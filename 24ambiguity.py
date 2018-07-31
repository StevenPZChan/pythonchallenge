import os
import zipfile
from io import BytesIO

import requests
from PIL import Image

header = {'Authorization': 'Basic YnV0dGVyOmZseQ==', }  # 'YnV0dGVyOmZseQ==' is base64.encode('butter:fly')
response = requests.get('http://www.pythonchallenge.com/pc/hex/maze.png', headers=header)
img = Image.open(BytesIO(response.content))

maze = []
for y in range(img.height):
    # 0 for road and 1 for wall
    maze.append(list(0 if img.getpixel((x, y))[2] else 1 for x in range(img.width)))
print(maze)

# the way out of maze
path = [(img.width - 2, 1)]
# never again
footprint = []
# down left up right
steps = ((0, 1), (-1, 0), (0, -1), (1, 0))
# entrance
x, y = path[-1]

while x != 1 or y != img.height - 2:
    # horizontal vertical
    for h, v in steps:
        if maze[y + v][x + h] and (x + h, y + v) not in footprint:
            path.append((x + 2 * h, y + 2 * v))  # this maze is step-2
            footprint.append((x + h, y + v))
            break
    else:
        path.pop()
    # location
    x, y = path[-1]
print(path)
# with open('path','wb') as f:
#     pickle.dump(path,f)

data = []
for p in path:
    data.append(img.getpixel(p)[0])

with open('maze.zip', 'wb') as f:
    f.write(bytes(data))
if not os.path.exists('maze'):
    os.makedirs('maze')
with zipfile.ZipFile('maze.zip', 'r') as f:
    for file in f.namelist():
        f.extract(file, 'maze')  # lake
