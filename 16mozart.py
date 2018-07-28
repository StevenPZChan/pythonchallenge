from io import BytesIO

import requests
from PIL import Image

header = {'Authorization': 'Basic aHVnZTpmaWxl', }
response = requests.get('http://www.pythonchallenge.com/pc/return/mozart.gif', headers=header)
img = Image.open(BytesIO(response.content))
img = img.convert('RGB')

img_new = Image.new('RGB', img.size)

for y in range(img_new.height):
    symbol_pos = [x for x in range(img.width) if
        img.getpixel((x, y))[0] == img.getpixel((x, y))[2] == 255 and img.getpixel((x, y))[1] == 0]
    move_style = list(range(img_new.width))
    move_style = move_style[symbol_pos[2]:] + move_style[:symbol_pos[2]]
    for x in range(img_new.width):
        img_new.putpixel((x, y), img.getpixel((move_style[x], y)))

img_new.show()  # romance
