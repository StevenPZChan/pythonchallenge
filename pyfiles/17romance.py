import bz2
import re
import xmlrpc.client

import requests

header = {'Authorization': 'Basic aHVnZTpmaWxl', }
response = requests.get('http://www.pythonchallenge.com/pc/return/romance.html', headers=header)
# cookies: info=you+should+have+followed+busynothing...;
# wikiticket=%D2%27%A6%B5%14a%0A%06%D9%C0%7F%BA%A5_%D2%93Q%EB%1B%02z
# small image is image in challenge 4: nothing-linkedlist --> try busynothing

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
busynothing = 12345  # should start from 12345 for cookie comeback
cookies = []
for i in range(400):
    response = requests.get(url + str(busynothing))
    data = response.content.decode('utf-8')
    number = re.findall(r'nothing is (\d+)', data)
    cookies.extend(x.replace('%', r'\x').replace('+', ' ') for x in response.cookies.values())
    if number:
        busynothing = number[0]
    else:
        break
    print(data)
print("".join(cookies))  # BZh91AY... --> bz2

print(bz2.decompress("".join(cookies).encode('utf-8').decode('unicode_escape').encode('latin1')))
# is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.
# --> phone(Mozart's father: Leopold) and use cookies("info=the flowers are on their way") to get the response

server = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
result = server.phone("Leopold")  # Mozart's father
print(result)  # 555-VIOLIN

cookie = {'info': 'the+flowers+are+on+their+way'}
response = requests.get('http://www.pythonchallenge.com/pc/stuff/violin.php', cookies=cookie)
print(response.content)  # oh well, don\'t you dare to forget the balloons.
