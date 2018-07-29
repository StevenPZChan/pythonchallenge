import base64
import os
import re
import wave
import winsound

import requests

header = {'Authorization': 'Basic YnV0dGVyOmZseQ==', }  # 'YnV0dGVyOmZseQ==' is base64.encode('butter:fly')
response = requests.get('http://www.pythonchallenge.com/pc/hex/bin.html', headers=header)

audio_content = re.findall(r'base64\s*(.+?=)[-]+', response.text.replace('\n', ''), re.S)

if not os.path.exists('indian'):
    os.makedirs('indian')
if not os.path.exists('indian/indian.wav'):
    with open('indian/indian.wav', 'wb') as f:
        f.write(base64.b64decode(audio_content[0].encode('utf-8')))

winsound.PlaySound('indian/indian.wav', winsound.SND_FILENAME)  # sorry
# sorry.html --> nothing useful
# --> indian probably means little endian, so reverse each sample in wav file

with wave.open('indian/indian.wav', 'rb') as indian:
    nchannels, sampwidth, framerate, nframes = indian.getparams()[:4]
    data = indian.readframes(nframes)
    split_data = [data[i:i + sampwidth] for i in range(0, len(data), sampwidth)]
    with wave.open('indian/endian.wav', 'wb') as endian:
        endian.setnchannels(nchannels)
        endian.setsampwidth(sampwidth)
        endian.setframerate(framerate)
        endian.writeframes(b"".join(x[::-1] for x in split_data))

winsound.PlaySound('indian/endian.wav', winsound.SND_FILENAME)  # you are an idiot, hahaha...
