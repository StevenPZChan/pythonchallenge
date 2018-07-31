import re

import requests

header = {'Authorization': 'Basic YnV0dGVyOmZseQ==', }  # 'YnV0dGVyOmZseQ==' is base64.encode('butter:fly')
response = requests.get('http://www.pythonchallenge.com/pc/hex/bonus.html', headers=header)

comments = re.findall(r'<!--(.*?)-->', response.text.replace('\n', ''), re.S)
print(comments)
# 'TODO: do you owe someone an apology? now it is a good time totell him that you are sorry. Please show good manners
#  althoughit has nothing to do with this level.'
# " \tit can't find it. this is an undocumented module. "
# 'va gur snpr bs jung?'

# webpage title is 'what is this module' --> import 'this' module

import this  # 'this' module is encoded by this.d dictionary(look inside)

print("".join([this.d.get(c, c) for c in 'va gur snpr bs jung?']))  # in the face of ambiguity
