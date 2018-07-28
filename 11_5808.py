from io import BytesIO

import requests
from PIL import Image

header = {'Authorization': 'Basic aHVnZTpmaWxl', }
response = requests.get('http://www.pythonchallenge.com/pc/return/cave.jpg', headers=header)
img = Image.open(BytesIO(response.content))

width, height = img.size
img_new = Image.new('RGB', (width // 2, height // 2))

odd = 1
even = 0
for x in range(width):
    for y in range(height):
        if x % 2 == odd and y % 2 == odd:  # x % 2 == even and y % 2 == even
            # multiplied by 5 to increase contrast
            img_new.putpixel((x // 2, y // 2), tuple(5 * p for p in img.getpixel((x, y))))

img_new.show()  # evil
