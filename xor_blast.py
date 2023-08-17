import binascii

a = [0x37, 0x0a, 0x05, 0x30, 0x3c, 0x29, 0x0e, 0x04, 0x50, 0x05, 0x03, 0x1c, 0x2b, 0x18, 0x58, 0x47, 0x3a, 0x5f, 0x05,
     0x21, 0x17, 0x03, 0x2c, 0x39, 0x23, 0x0f, 0x00, 0x5d, 0x1e, 0x17]
# a = [168, 50, 29, 174, 100, 169, 53, 7, 166, 240, 228, 211, 146, 169, 173, 208, 169, 199, 135, 37, 85, 8, 6, 90, 151, 210, 202, 28, 196, 245, 35, 236, 18, 85, 214, 191, 135, 206, 51, 121, 180, 189]
#
# a = bytearray(b'E`}J]OrQF[V8zV:hzpV}fVF[t')
#
# a = binascii.unhexlify(b'217137cb58e28521a1ae0264b6b9adc6a1aeb34937a3e2d657791fb4e48d4bdf1459ffa79bb3fe8ea')
table = [chr(i) for i in range(0x20, 0x7F)]
for i in range(256):
    # 异或固定数字
    for j in range(len(a)):
        if chr((a[j] ^ i) & 0xff) not in table:
            break
    else:
        print(f"a[i] ^ {str(i):^10}: ", end='')
        for j in range(len(a)):
            print(chr((a[j] ^ i) & 0xff), end='')
        print()

    # 异或下标+固定数字
    for j in range(len(a)):
        if chr((a[j] ^ (j + i)) & 0xff) not in table:
            break
    else:
        print(f"a[i] ^ (i + {str(i):^3}) : ", end='')
        for j in range(len(a)):
            print(chr((a[j] ^ (j + i)) & 0xff), end='')
        print()

    # 异或下标*固定数字
    for j in range(len(a)):
        if chr((a[j] ^ (j * i)) & 0xff) not in table:
            break
    else:
        print(f"a[i] ^ (i * {str(i):^3}) : ", end='')
        for j in range(len(a)):
            print(chr((a[j] ^ (j * i)) & 0xff), end='')
        print()
