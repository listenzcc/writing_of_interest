# Script of Summary .md Files
# To Generate README.md file

import os

# Setup the working directory
WD = os.path.dirname(__file__)

# Folders of potential .md files
folders = ['FirstThingFirst']

# Contents of Final README.md
contents = [open(os.path.join(WD, 'README-head.md')).read()]

for folder in folders:
    for md in [e for e in os.listdir(os.path.join(WD, folder)) if e.endswith('.md')]:
        path = os.path.join(WD, folder, md)
        contents.append(open(path).read())

content = '\n'.join(contents)

with open(os.path.join(WD, 'README.md'), 'w') as f:
    f.write(content)

print(content)

print('All Done')
