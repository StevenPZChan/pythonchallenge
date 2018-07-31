import os
from io import BytesIO

import requests
from PIL import Image, ImageFile

header = {'Authorization': 'Basic aHVnZTpmaWxl', }
response = requests.get('http://www.pythonchallenge.com/pc/return/evil2.gfx', headers=header)
data = response.content
print(requests.get('http://www.pythonchallenge.com/pc/return/evil4.jpg', headers=header).content)
# Bert is evil! go back!  -->Hints for next problem

if not os.path.exists('evil'):
    os.makedirs('evil')

ImageFile.LOAD_TRUNCATED_IMAGES = True
for i in range(5):
    img = Image.open(BytesIO(data[i::5]))
    img.save('evil/pic{0}.{1}'.format(i, img.format.lower()))
    img.show()

# disproportional  <del>ity</del>
