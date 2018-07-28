from io import BytesIO

import requests
from PIL import Image

header = {'Authorization': 'Basic aHVnZTpmaWxl', }
response = requests.get('http://www.pythonchallenge.com/pc/return/wire.png', headers=header)
img = Image.open(BytesIO(response.content))

img_new = Image.new('RGB', (100, 100))
walk_around = sorted(list(range(1, 101)) + list(range(1, 100)), reverse=True)

direction = 0  # 0 : right, 1 : down, 2 : left, 3 : up
x, y = -1, 0
total = 0
for i in walk_around:
    for j in range(i):
        if direction == 0:
            x += 1
        elif direction == 1:
            y += 1
        elif direction == 2:
            x -= 1
        else:
            y -= 1
        img_new.putpixel((x, y), img.getpixel((total, 0)))
        total += 1
    direction = (direction + 1) % 4

img_new.show()  # cat
