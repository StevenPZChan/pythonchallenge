import re
from urllib import request

from lxml import etree

script = request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php")
data = script.read().decode("utf-8")

code = etree.HTML(data).xpath('/html/body/center/a/@href')
script = request.urlopen("http://www.pythonchallenge.com/pc/def/" + code[0])
data = script.read().decode("utf-8")

for i in range(400):
    number = re.findall(r'nothing is (\d+)', data)
    if re.findall(r'Divide by two', data):
        code = str(int(code) / 2)
    elif re.findall(r'\.html', data):
        break
    else:
        code = number[0]
    script = request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + code)
    data = script.read().decode("utf-8")
    print(data)

# peak.html
