import base64, base36, base58, base91, py3base92, base128
# pip install base36 base58 base91 base128
# https://github.com/Gu-f/py3base92


# base32
print()
print('base32:')

data = 'flag{123456}'
c = base64.b32encode(data.encode())
print(c)
m = base64.b32decode(c)
print(m)


# base36
print()
print('base36:')

c = base36.loads('flag123456')
print(c)
m = base36.dumps(int(c))
print(m)


# base58
print()
print('base58:')

c = base58.b58encode(data.encode())
print(c)
m = base58.b58decode(c)
print(m)


# base85
print()
print('base85:')

c = base64.a85encode(data.encode('utf-8'))
print(c)
m = base64.a85decode(c)
print(m)


# base91
print()
print('base91:')

c = base91.encode(data.encode('utf-8'))
print(c)
m = base91.decode(c).decode()
print(m)


# base92
print()
print('base92:')

c = py3base92.b92encode(data.encode())
print(c)
m = py3base92.b92decode("F#S<YRW^.DFd=<\\")
print(m)


# base128
print()
print('base128:')

b128 = base128.base128(chars=None, chunksize=7)
c = list(b128.encode(data.encode(encoding="utf-8")))
print(c)
m = b''.join(b128.decode(c)).decode()
print(m)
