
import os
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG)


splitter = ['.', '\n']


def strip(tag, splitter=splitter):
    '''
    Get text from the [tag] and strip it
    - @tag: The HTML tag object in soup
    - @splitter: The splitter used to separate the sentences
    '''
    s = tag.get_text().strip()
    # Regularize the splitter
    for sp in splitter:
        s = s.replace(sp, '\n')
    # Generate output list and return it
    return [e.strip() for e in s.split('\n') if e.strip()]


def all_sentences(soup):
    '''
    Get all sentences from the [soup]
    - @soup: The soup of interest
    '''
    found = [strip(tag) for tag in soup.find_all('p')]
    sentences = set()
    for entry in found:
        for f in entry:
            sentences.add(f.lower())
    return sentences


def mkdir(folder):
    '''
    Create [folder] if it is necessary
    - @folder: The path of folder to be created
    '''
    if not os.path.isdir(folder):
        os.mkdir(folder)
    assert(os.path.isdir(folder))


class Inventory(object):
    '''
    Inventory manager
    '''

    def __init__(self, fpath, root_url, inventory_folder):
        '''
        - @fpath: The path of DataFrame of inventory
        - @root_url: The root_url of the web site
        - @inventory_folder: The folder of the .html file will be stored to
        '''
        self.fpath = fpath
        self.root_url = root_url
        self.inventory_folder = inventory_folder

        # Prepare inventory
        if os.path.isfile(fpath):
            df = pd.read_json(fpath)
            logging.debug(f'Read inventory from {fpath}')
        else:
            df = pd.DataFrame(columns=['url', 'path'])
            logging.debug(
                f'Empty inventory is created since {fpath} is invalid')

        self.df = df

        logging.info('Inventory initialized')

    def add(self, url):
        '''
        Add entry of [url] to inventory
        - @url: The url of the .html file
        '''
        # Assert the [url] is in the same domain as the [root_url]
        assert(url.startswith(self.root_url))

        # Regularize [name], it is like "a/b/c/d"
        name = url[len(self.root_url):].strip()
        while '//' in name:
            name.replace('//', '/')
        if name.startswith('/'):
            name = name[1:]

        # Make structure step-by-step
        folder = self.inventory_folder

        steps = name.split('/')
        for s in steps[:-1]:
            folder = os.path.join(folder, s)
            mkdir(folder)

        if steps[-1].endswith('.html'):
            path = os.path.join(folder, steps[-1])
        else:
            folder = os.path.join(folder, steps[-1])
            mkdir(folder)
            path = os.path.join(folder, 'index.html')

        if url not in self.df['url'].values:
            self.df = self.df.append(dict(url=url, path=path),
                                     ignore_index=True)
            logging.info(f'New inventory is added, {url}: {path}')
        else:
            logging.warning(f'{url} exists')

        return path

    def display(self):
        '''Display inventory'''
        print(self.df)

    def save(self):
        '''Save the inventory to disk'''
        self.df.to_json(self.fpath)
