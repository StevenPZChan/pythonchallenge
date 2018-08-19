import re
from io import BytesIO

import requests
from PIL import Image

response = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
img = Image.open(BytesIO(response.content))
# img.crop((0,43,608,52)).show()
# print(list(img.getpixel((x, y))[:3] for x in range(608) for y in range(43, 52)))
width, height = img.size
cd = [chr(img.getpixel((x, y))[0]) if img.getpixel((x, y))[0] == img.getpixel((x, y))[1] == img.getpixel((x, y))[
    2] else chr(0) for y in range(height) for x in range(width)]

hided_text = re.findall(r'(.)\1{4,6}', "".join(cd))
encoded_str = re.findall(r'(\d+)', "".join(hided_text))
decoded_str = [chr(int(c)) for c in encoded_str]
simplified_str = re.findall(r'(\w+?)\1+', "".join(decoded_str))
print(simplified_str)  # integrity
