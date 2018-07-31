import os
import wave

import requests
from PIL import Image

header = {'Authorization': 'Basic YnV0dGVyOmZseQ==', }  # 'YnV0dGVyOmZseQ==' is base64.encode('butter:fly')

if not os.path.exists('lake'):
    os.makedirs('lake')
for i in range(1, 26):
    response = requests.get(f'http://www.pythonchallenge.com/pc/hex/lake{i}.wav', headers=header)
    with open(f'lake/{i:02}.wav', 'wb') as f:
        f.write(response.content)
# each wav file has 10800 frames, each 3 for a pixel data, so each file represents an image of 60*60

img = Image.new('RGB', (5 * 60, 5 * 60))
for i in range(1, 26):
    with wave.open(f'lake/{i:02}.wav', 'rb') as f:
        data = f.readframes(f.getnframes())
    piece = Image.frombytes('RGB', (60, 60), data)
    img.paste(piece, ((i - 1) % 5 * 60, (i - 1) // 5 * 60))

img.show()  # decent
