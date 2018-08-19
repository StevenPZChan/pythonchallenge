import bz2
import re

import requests

response = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html')
url_text = response.content.decode('utf-8')
un = re.findall(r"un: '(.+)'", url_text)[0]
pw = re.findall(r"pw: '(.+)'", url_text)[0]

print(un)
print(pw)
print(bz2.decompress(un.encode('utf-8').decode('unicode_escape').encode('latin1')))
print(bz2.decompress(pw.encode('utf-8').decode('unicode_escape').encode('latin1')))  # huge, file
