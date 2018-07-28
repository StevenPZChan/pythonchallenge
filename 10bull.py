import re

import requests

header = {'Authorization': 'Basic aHVnZTpmaWxl', }
response = requests.get('http://www.pythonchallenge.com/pc/return/sequence.txt', headers=header)
url_text = response.content.decode('utf-8')  # a = [1, 11, 21, 1211, 111221,


def count_num(num):
    num_str = str(num)
    m = re.findall(r'((\d)\2*)', num_str)
    count = "".join([str(len(pat[0])) + pat[1] for pat in m])
    return int(count)


a = [1]
for i in range(30):
    a.append(count_num(a[-1]))
# print(a)
print(len(str(a[30])))  # 5808
