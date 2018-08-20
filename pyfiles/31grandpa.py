# search image on Internet --> Koh Samui in Thailand
# user:password = kohsamui:thailand
from io import BytesIO

import requests
from PIL import Image

header = {'Authorization': 'Basic a29oc2FtdWk6dGhhaWxhbmQ=', }
response = requests.get('http://www.pythonchallenge.com/pc/rock/mandelbrot.gif', headers=header)
img = Image.open(BytesIO(response.content))

left, top, width, height = 0.34, 0.57, 0.036, 0.027
iterations = 128
img_new = img.copy()


def iter_point(c):
    z = c
    i = 0
    for i in range(iterations):
        if abs(z) > 2:
            break
        z = z * z + c
    return i


def draw_mandelbrot(m_left, m_top, m_width, m_height):
    mandelbrot = []
    for y in range(img.height - 1, -1, -1):
        for x in range(img.width):
            c = complex(m_left + x * m_width / img.width, m_top + y * m_height / img.height)
            mandelbrot.append(iter_point(c))

    img_new.putdata(mandelbrot)
    img_new.show()


draw_mandelbrot(left, top, width, height)  # almost the same

img_diff = [p[0] - p[1] for p in zip(img.getdata(), img_new.getdata()) if p[0] != p[1]]
print(img_diff)
ufo_message = len(img_diff)


def prime_factor(n):
    n = int(n)
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print(i, end=' ')
            print("*", end=' ')
            return prime_factor(n // i)
    print(n)


print('total:', ufo_message, '=', end=' ')
prime_factor(ufo_message)  # 1679 = 23 * 73

img_message = Image.new('L', (23, 73))
for p in range(ufo_message):
    img_message.putpixel((p % img_message.width, p // img_message.width), 255 if img_diff[p] > 0 else 0)

img_message.show()  # the image is Arecibo message
