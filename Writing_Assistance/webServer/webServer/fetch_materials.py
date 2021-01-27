# Fetch material from websites

# %%
import os
import requests
import threading

from tqdm.auto import tqdm
from bs4 import BeautifulSoup

from local_toolbox import mkdir, Inventory

# %%
# Settings
root_url = 'https://www.statlect.com/'
inventory_folder = 'www.statlect.com'
inventory_name = 'www.statlect.com.json'

# %%
# Prepare

mkdir(inventory_folder)

inventory = Inventory(inventory_name, root_url, inventory_folder)

# %%
attrs = {'class': ['menu3', 'index2']}


def fetch_all(url, root_url=root_url, attrs=attrs, depth=0):
    print(f'-- {url}')
    if depth > 10:
        return 0

    path = inventory.add(url)

    if os.path.isfile(path):
        text = open(os.path.join(os.path.abspath('.'), path)).read()
    else:
        text = requests.get(url).text

    with open(path, 'w') as f:
        f.write(text)

    soup = BeautifulSoup(text, features='lxml')
    for m in tqdm(soup.find_all(attrs=attrs)):
        href = m.get('href', None)

        # Continue if href is invalid
        if href is None:
            continue

        # t = threading.Thread(target=fetch_all,
        #                      args=[root_url+href],
        #                      kwargs=dict(depth=depth+1))
        # t.start()
        fetch_all(root_url + href, depth=depth+1)


fetch_all(root_url)

# %%
# resp = requests.get(root_url)
# path = inventory.add(root_url)
# with open(path, 'w') as f:
#     f.write(resp.text)

# soup = BeautifulSoup(resp.text)

# for m in tqdm(soup.find_all(attrs=attrs)):
#     href = m.get('href', None)

#     # Continue if href is invalid
#     if href is None:
#         continue

#     url = root_url + href
#     path = inventory.add(url)

#     # Continue if [path] exists
#     if os.path.isfile(path):
#         continue

#     _resp = requests.get(url)
#     with open(path, 'w') as f:
#         f.write(_resp.text)

# %%
inventory.save()

# %%
inventory.display()

# %%
