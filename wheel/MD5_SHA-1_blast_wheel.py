import hashlib


def check(s, md5):
    if hashlib.md5(s).hexdigest() == md5:
        return True
    return False


md = '5a3ebb487ad0046e52db00570339aace'
flag = bytearray(b'Y0uReallyKn0wB4s')
# di = b'0123456789qwertyuiopasdfghjklzxcvbnm'
di = range(0x20, 0x7F)
ch = [chr(i) for i in range(0x20,0x7f)]

def solve(s, idx, totallenth):
    if idx == totallenth:
        if check(s.encode(),md):
            print(s)
            exit()
        else:
            return 0

    for i in range(len(ch)):
        solve(s + ch[i], idx + 1, totallenth)

a = 'Y0uReallyKn0wB4s'
solve(a, len(a), len(a) + 4)

# 纯数字
# win = 0
# for i in range(100000, 999999):
#     s = str(i)
#     x = hashlib.md5(s.encode())
#     if x.hexdigest() == "c8837b23ff8aaa8a2dde915473ce0991":
#         print("Successfully!")
#         win = aaa
#         print(str(i))
#         break
# if not win:
#     print("Failure!")
