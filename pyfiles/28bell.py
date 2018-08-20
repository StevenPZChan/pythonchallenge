import itertools
from io import BytesIO

import requests
from PIL import Image

header = {'Authorization': 'Basic cmVwZWF0OnN3aXRjaA==', }
response = requests.get('http://www.pythonchallenge.com/pc/ring/bell.png', headers=header)
img = Image.open(BytesIO(response.content))

# RING-RING-RING --> means green --> extract green channel
green = [img.getpixel((x, y))[1] for y, x in itertools.product(range(img.height), range(img.width))]

# title is 'many pairs ring-ring' --> make them pairs
green_pairs = [green[i:i + 2] for i in range(0, len(green), 2)]

# find most pairs has a difference of 42
outlier = list(filter(lambda p: 42 != abs(p[0] - p[1]), green_pairs))

diff_outlier = [abs(p[0] - p[1]) for p in outlier]
print(bytes(diff_outlier))  # 'whodunnit().split()[0] ?'


def whodunnit():
    """:return who done it -- """
    return 'Guido van Rossum'


print(whodunnit().split()[0])  # Guido
