import re

import requests

from nonogram import NonogramSolver

header = {'Authorization': 'Basic a29oc2FtdWk6dGhhaWxhbmQ=', }


def split_data(data):
    splits = {}
    key = None
    for f in data:
        if re.match(r'# Dimension', f):
            key = 'd'
            splits[key] = []
        elif re.match(r'# Horizon', f):
            key = 'h'
            splits[key] = []
        elif re.match(r'# Vertical', f):
            key = 'v'
            splits[key] = []
        elif f:
            d = [int(s) for s in f.split()]
            splits[key].append(d)

    print(splits)
    return splits


response = requests.get('http://www.pythonchallenge.com/pc/rock/warmup.txt', headers=header)
split = split_data(response.text.splitlines())
solver = NonogramSolver(split['d'][0], split['h'], split['v'])
solver.solve()
solver.solution.show()  # an arrow up --> up.html

response = requests.get('http://www.pythonchallenge.com/pc/rock/up.txt', headers=header)
split = split_data(response.text.splitlines())
solver = NonogramSolver(split['d'][0], split['h'], split['v'])
solver.solve()
solver.solution.show()  # a snake --> python.html

#  "free software" is a matter of liberty, not price. To understand the concept,
# you should think of "free" as in "free speech", not as in "free beer".
