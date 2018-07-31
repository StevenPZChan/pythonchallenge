import bz2
import re

import requests

header = {'Authorization': 'Basic cmVwZWF0OnN3aXRjaA==', }
response = requests.get('http://www.pythonchallenge.com/pc/ring/guido.html', headers=header)

hided_info = re.findall(r'</html>\n(.*)', response.text, re.S)
print(hided_info[0].splitlines())

shaped_info = [len(l) for l in hided_info[0].splitlines()]
print(bytes(shaped_info))
print(bz2.decompress(bytes(shaped_info)))  # "Isn't it clear? I am yankeedoodle!"
