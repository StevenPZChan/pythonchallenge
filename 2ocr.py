import re
from urllib import request

script = request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
data = script.read().decode("utf-8")

finded_str = re.findall(r'<!--(.*?)-->', data, re.S)
encoded_str = finded_str[1]

strcount = {}
for c in encoded_str:
    strcount[c] = encoded_str.count(c)

rare_char = [k for k, v in strcount.items() if v < 3]
print("".join(rare_char))  # equality
