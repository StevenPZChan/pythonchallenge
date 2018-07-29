import itertools
from collections import Counter
from io import BytesIO

import requests
from PIL import Image, ImageSequence, ImageDraw

header = {'Authorization': 'Basic YnV0dGVyOmZseQ==', }  # 'YnV0dGVyOmZseQ==' is base64.encode('butter:fly')
response = requests.get('http://www.pythonchallenge.com/pc/hex/white.gif', headers=header)
imgs = Image.open(BytesIO(response.content))

brighter_points = []
for img in ImageSequence.Iterator(imgs):
    pos = list(img.getdata()).index(img.getextrema()[1])
    brighter_points.append((pos % img.width, pos // img.width))

print(brighter_points)  # seems like random walk

c = Counter()
for p in brighter_points:
    c[p] += 1

num = c[(100, 100)]
img_new = Image.new('RGB', (50 * num, 50))
draw = ImageDraw.Draw(img_new)
n = 0
points = []
for p in brighter_points:
    if p == (100, 100):
        if n > 0:
            draw.line(points, 'red', 3)
        points = [(50 * n + 25, 25)]
        n += 1
    else:
        d = [x - 100 for x in p]
        points.append((points[-1][0] + d[0], points[-1][1] + d[1]))

draw.line(points, 'red', 3)
img_new.show()  # bonus
