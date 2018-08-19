import bz2
import keyword
from io import BytesIO

import requests
from PIL import Image

header = {'Authorization': 'Basic YnV0dGVyOmZseQ==', }  # 'YnV0dGVyOmZseQ==' is base64.encode('butter:fly')
response = requests.get('http://www.pythonchallenge.com/pc/hex/zigzag.gif', headers=header)
img = Image.open(BytesIO(response.content))
palette = [img.getpalette()[p:p + 3] for p in range(0, len(img.getpalette()), 3)]

raw_data = img.tobytes()
trans_data = b''.join(bytes((palette[c][0],)) for c in raw_data)

img_new = img.copy()
data_diff = [b'', b'']
for i in range(1, len(raw_data)):
    if raw_data[i] != trans_data[i - 1]:
        data_diff[0] += bytes((raw_data[i],))
        data_diff[1] += bytes((trans_data[i - 1],))
        img_new.putpixel((i % img.width, i // img.width), 255)
    else:
        img_new.putpixel((i % img.width, i // img.width), 0)

print(data_diff)  # first is bz2 compressed
img_new.show()  # not key word, 'busy' means bz
decoded_str = bz2.decompress(data_diff[0])
print(decoded_str)  # '../ring/bell.html del assert repeat raise or class is exec return except print return switch
# from exec repeat else not while assert or class class break except assert yield finally ..

# remove keywords in python, but print, exec used to be keyword
notkeywords = set(decoded_str.decode('utf-8').split()) - set(keyword.kwlist) - {'print', 'exec'}
for word in decoded_str.decode('utf-8').split():
    if not notkeywords:
        break
    if word in notkeywords:
        print(word)
        notkeywords -= {word}

# ../ring/bell.html
# repeat
# switch
