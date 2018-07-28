import pickle
from urllib import request

script = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = script.read()
encoded = pickle.loads(data)

for pat in encoded:
    print("".join([x[0] * x[1] for x in pat]), end="")
    print()

# channel
