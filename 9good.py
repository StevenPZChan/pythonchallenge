import re
from io import BytesIO

import requests
from PIL import Image, ImageDraw
from lxml import etree

header = {'Authorization': 'Basic aHVnZTpmaWxl', }
response = requests.get('http://www.pythonchallenge.com/pc/return/good.html', headers=header)
url_text = response.content.decode('utf-8')

img_path = etree.HTML(url_text).xpath('/html/body/center/img/@src')[0]
img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/return/' + img_path, headers=header).content))
# img.show()

extracted_info = re.findall(r'first:.*?((?:\d+.)+).*?second:.*?((?:\d+.)+)', url_text.replace('\n', ''))
first = [int(x) for x in re.findall(r'(\d+)', extracted_info[0][0])]
second = [int(x) for x in re.findall(r'(\d+)', extracted_info[0][1])]

draw = ImageDraw.Draw(img)
draw.line(first, 'red', 5)
draw.line(second, 'blue', 5)
img.show()  # bull
