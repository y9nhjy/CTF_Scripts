import hashlib


def check(s, md):
    if hashlib.md5(s).hexdigest() == md:
        return True
    return False


md = '5a3ebb487ad0046e52db00570339aace'
flag = bytearray(b'Y0uReallyKn0wB4s')
# di = b'0123456789qwertyuiopasdfghjklzxcvbnm'
di = range(0x20, 0x7F)
for j1 in di:
    # flag.insert(13, j1)
    flag.append(j1)
    for j2 in di:
        flag.append(j2)
        for j3 in di:
            flag.append(j3)
            for j4 in di:
                flag.append(j4)
                if check(flag, md):
                    print("Right flag :", flag.decode())
                    exit()
                flag.pop()
            flag.pop()
        flag.pop()
    print(flag)
    # del flag[13]
    flag.pop()

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
