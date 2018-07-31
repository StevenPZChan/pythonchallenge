import requests
from PIL import Image

header = {'Authorization': 'Basic cmVwZWF0OnN3aXRjaA==', }
response = requests.get('http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv', headers=header)
with open('yankeedoodle.csv', 'wb') as f:
    f.write(response.content)

with open('yankeedoodle.csv', 'r') as f:
    data = f.read().replace('\n', '').split(',')

num_data = len(data)


def prime_factor(n):
    n = int(n)
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print(i, end=' ')
            print("*", end=' ')
            return prime_factor(n // i)
    print(n)


print('total:', num_data, '=', end=' ')
prime_factor(num_data)  # 7367 = 53 * 139

img = Image.new('F', (139, 53))
for i in range(num_data):
    img.putpixel((i // img.height, i % img.height), 256 * float(data[i]))
img.show()  # n=str(x[i])[5]+str(x[i+1])[5]+str(x[i+2])[6]

x = [f'{float(s):.5f}' for s in data]
encoded_str = [str(x[i])[5] + str(x[i + 1])[5] + str(x[i + 2])[6] for i in range(0, num_data // 3 * 3, 3)]
print(encoded_str)
print(bytes(int(i) for i in encoded_str))

# 'So, you found the hidden message.\nThere is lots of room here for a long message, but we only need
# very little space to say "look at grandpa", so the rest is just garbage. \nVTZ.l
