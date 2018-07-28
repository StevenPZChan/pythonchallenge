import re
from urllib import request

script = request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
data = script.read().decode("utf-8")

finded_str = re.findall(r'<!--(.*?)-->', data, re.S)
encoded_str = finded_str[0]

re_str = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
small_letter = re.findall(re_str, encoded_str)
print("".join(small_letter))  # linkedlist
