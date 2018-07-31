import os
import re
import zipfile

import requests

filename = 'http://www.pythonchallenge.com/pc/def/channel.zip'
if not os.path.exists('channel.zip'):
    r = requests.get(filename)
    with open('channel.zip', 'wb') as f:
        f.write(r.content)
#
# if not os.path.exists('channel'):
#     os.makedirs('channel')
#     fz = zipfile.ZipFile('channel.zip', 'r')
#     for file in fz.namelist():
#         fz.extract(file, 'channel')

nothing = 90052
comment = b''
with zipfile.ZipFile('channel.zip', 'r') as fz:
    for i in range(1000):
        comment += fz.getinfo('{0}.txt'.format(nothing)).comment
        with fz.open('{0}.txt'.format(nothing), 'r') as f:
            data = f.read().decode('utf-8')

        print(data)
        scratch = re.findall(r'nothing is (\d+)', data)
        if scratch:
            nothing = scratch[0]
        else:
            break

print(comment.decode('utf-8'))  # hockey, oxygen
