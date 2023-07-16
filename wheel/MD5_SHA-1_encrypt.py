import hashlib

# c = 'U_G07_th3_k3y!'
c = '172.30.0.0'
md5 = hashlib.md5(c.encode('ascii')).hexdigest()
print(md5)
# sha1 = hashlib.sha1(c.encode('ascii')).hexdigest()
# print(sha1)
