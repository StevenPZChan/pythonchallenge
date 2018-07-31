import math
from collections import Counter
from io import BytesIO

import requests
from PIL import Image

header = {'Authorization': 'Basic a29oc2FtdWk6dGhhaWxhbmQ=', }
response = requests.get('http://www.pythonchallenge.com/pc/rock/beer2.png', headers=header)
img = Image.open(BytesIO(response.content))

c = Counter()
for i in img.getdata():
    c[i] += 1
print(c)

bars = sorted(c.keys(), reverse=True)
raw_data = img.getdata()
while bars:
    side = int(math.sqrt(len(raw_data)))
    img_new = Image.new('L', (side, side))
    filtered = [255 if x == bars[0] else 0 for x in raw_data]
    img_new.putdata(filtered)
    img_new.show()
    raw_data = list(filter(lambda x: x not in bars[:2], raw_data))
    bars = bars[2:]

# xxxxxxxxxxxxvine ga rwin e mo ld i no slo
# with square: gremlins

# If you are blinded by the light,
#      -- If the brightest pixels (the light) prevent you from
#         seeing anything else [By the way, they do so not
#         because they are bright, but because they move the
#         other pixels to random places],
# remove its power, with its might.
#      -- then you should delete (remove) the brightest (power)
#         and the next brightest (might) pixels.
# Then from the ashes, fair and square,
#      -- Then the seemingly random noise (the ashes), can be put
#         in a square (square) in which the brightest (fair) pixels,
# another truth at you will glare.
#      -- will look (glare) like another letter (truth).
#      Don't be too hasty, though: only letters inside square frames
#      are truly fair.
