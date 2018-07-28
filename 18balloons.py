import difflib
import gzip
import itertools
import os
from io import BytesIO

import requests
from PIL import Image

header = {'Authorization': 'Basic aHVnZTpmaWxl', }
response = requests.get('http://www.pythonchallenge.com/pc/return/balloons.jpg', headers=header)
img = Image.open(BytesIO(response.content))

# img_left = img.crop((0, 0, img.width // 2, img.height))
# img_right = img.crop((img.width // 2, 0, img.width, img.height))
#
# img_left.show()
# img_right.show()
#
# img_diff = Image.new('RGB', (img.width // 2, img.height))
# for y in range(img.height):
#     for x in range(img.width//2):
#         img_diff.putpixel((x,y),tuple(p[0]-p[1] for p in zip(img_left.getpixel((x,y)),img_right.getpixel((x,y)))))
#
# img_diff.show()  # brightness.html :(

filename = 'http://www.pythonchallenge.com/pc/return/deltas.gz'
if not os.path.exists('deltas.gz'):
    r = requests.get(filename, headers=header)
    with open('deltas.gz', 'wb') as f:
        f.write(r.content)
if not os.path.exists('deltas'):
    os.makedirs('deltas')
    with gzip.open('deltas.gz', 'r') as fz:
        with open('deltas/delta.txt', 'wb') as f:
            f.write(fz.read())

with open('deltas/delta.txt', 'r') as f:
    data = f.read()
    data_split_line = data.splitlines()
    data_left = list(x[:53] for x in data_split_line)
    data_right = list(x[56:] for x in data_split_line)

data_diff = difflib.Differ().compare(data_left, data_right)
same = []
first = []
second = []
for s in data_diff:
    data_str = s[2:]
    if s[0] == ' ':
        same.append(data_str)
    elif s[0] == '+':
        first.append(data_str)
    elif s[0] == '-':
        second.append(data_str)
    else:
        break


def lines_to_img(lines):
    img_bytes_str = itertools.chain(*(x.split() for x in lines))
    img_bytes = [int(x, 16) for x in img_bytes_str]
    return Image.open(BytesIO(bytes(img_bytes)))


img = lines_to_img(same)
img.save('deltas/same.{0}'.format(img.format.lower()))
img.show()  # ../hex/bin.html
img = lines_to_img(first)
img.save('deltas/first.{0}'.format(img.format.lower()))
img.show()  # butter
img = lines_to_img(second)
img.save('deltas/second.{0}'.format(img.format.lower()))
img.show()  # fly
