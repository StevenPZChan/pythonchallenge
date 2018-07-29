import os
import re
import zipfile

import requests

header = {'Authorization': 'Basic YnV0dGVyOmZseQ==', }  # 'YnV0dGVyOmZseQ==' is base64.encode('butter:fly')
response = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers=header)

private = []
for i in range(10):
    print(response.headers)
    if 'Content-Range' not in response.headers:
        break

    received = re.findall(r'bytes \d+-(\d+)/(\d+)', response.headers['Content-Range'])
    last_byte = int(received[0][0])
    total_bytes = int(received[0][1])
    header['Range'] = f'bytes={last_byte+1}-'
    response = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers=header)
    private.extend(response.content)

print(bytes(private))
# "Why don't you respect my privacy?\nwe can go on in this way for really long time.\nstop this!\ninvader! invader!\nok, invader. you are inside now. \n"

header['Range'] = f'bytes={total_bytes}-'
response = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers=header)
print(response.content)  # 'esrever ni emankcin wen ruoy si drowssap eht\n'
print(response.content[::-1])  # '\nthe password is your new nickname in reverse' --> redavni

received = re.findall(r'bytes (\d+)-(\d+)/\d+', response.headers['Content-Range'])
first_byte = int(received[0][0])
header['Range'] = f'bytes={first_byte-1}-'
response = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers=header)
print(response.content)  # 'and it is hiding at 1152983631.\n'

hided_info = re.findall(r'(\d+)', response.text)
header['Range'] = f'bytes={hided_info[0]}-'
response = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers=header)
print(response.content[:100])  # PKzip

with open('invader.zip', 'wb') as f:
    f.write(response.content)

if not os.path.exists('invader'):
    os.makedirs('invader')
fz = zipfile.ZipFile('invader.zip', 'r')
for file in fz.namelist():
    fz.extract(file, 'invader', pwd='redavni'.encode('utf-8'))
# Got level 21
