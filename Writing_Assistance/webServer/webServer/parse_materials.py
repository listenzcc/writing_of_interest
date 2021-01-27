# Parse materials

# %%
import pandas as pd

from tqdm.auto import tqdm
from bs4 import BeautifulSoup

from local_toolbox import all_sentences

# %%
# Debugger
# path = 'C:\\Users\\zcc\\Documents\\writing_of_interest\\Writing_Assistance\\webServer\\webServer\\www.statlect.com\\index.html'
# soup = BeautifulSoup(open(path).read())
# sentences = all_sentences(soup)
# sorted([e for e in sentences])

# %%
inventory = pd.read_json('www.statlect.com.json')
inventory = inventory.drop_duplicates('url', keep='first')
inventory.index = range(len(inventory))
inventory

# %%
dd = []

for j in tqdm(range(len(inventory))):
    path = inventory['path'][j]
    url = inventory['url'][j]

    soup = BeautifulSoup(open(path).read())
    unwanted = soup.find_all(attrs={'class': 'tableOfContents'})
    [e.extract() for e in unwanted]
    sentences = all_sentences(soup)

    d = pd.DataFrame(sentences)
    d.columns = ['sentence']
    d['path'] = path
    d['url'] = url
    dd.append(d)

data = pd.concat(dd)
data

# %%
data['length'] = data['sentence'].map(len)
data['count'] = data['sentence'].map(lambda x: len(x.split()))

data = data[data['length'] > 5]
data = data[data['count'] > 2]

data = data.sort_values(by='length', ascending=False)
data.index = range(len(data))

data.to_json('__inventory.json')
data

# %%
