import zlib
import bz2

logs = []


def my_decode(encoded_bytes):
    if encoded_bytes.startswith(b'x\x9c'):
        logs.append('.')
        return zlib.decompress(encoded_bytes)
    elif encoded_bytes.startswith(b'BZh'):
        logs.append('0')
        return bz2.decompress(encoded_bytes)
    elif encoded_bytes.endswith(b'\x9cx'):
        logs.append('\n')
        return zlib.decompress(encoded_bytes[::-1])
    else:
        print(encoded_bytes)  # 'sgol ruoy ta kool'
        print(encoded_bytes[::-1])  # 'look at your logs' --> add logs to function
        print("".join(logs))  # copper
        exit(0)


with open('invader/package.pack', 'rb') as f:
    data = f.read()

while True:
    data = my_decode(data)
    with open('invader/unpack', 'wb') as f:
        f.write(data)
