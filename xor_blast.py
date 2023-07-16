import binascii

a = [  0x46, 0x7A, 0x7B, 0x61, 0x4D, 0x7B, 0x61, 0x4D, 0x7C, 0x7D,
  0x66, 0x4D, 0x74, 0x7E, 0x73, 0x75, 0x4D, 0x20, 0x21, 0x21,
]
a = [168, 50, 29, 174, 100, 169, 53, 7, 166, 240, 228, 211, 146, 169, 173, 208, 169, 199, 135, 37, 85, 8, 6, 90, 151, 210, 202, 28, 196, 245, 35, 236, 18, 85, 214, 191, 135, 206, 51, 121, 180, 189]

a = bytearray(b'E`}J]OrQF[V8zV:hzpV}fVF[t')

a = binascii.unhexlify(b'217137cb58e28521a1ae0264b6b9adc6a1aeb34937a3e2d657791fb4e48d4bdf1459ffa79bb3fe8ea')
table = [chr(i) for i in range(0x20, 0x7F)]
for i in range(256):
    for j in range(len(a)):
        if chr((a[j] ^ (j + i)) & 0xff) not in table:
            break
    else:
        print("a[i] ^ (i + " + str(i) + '):')
        for j in range(len(a)):
            print(chr((a[j] ^ (j + i)) & 0xff), end='')
        print()


    for j in range(len(a)):
        if chr((a[j] ^ (i)) & 0xff) not in table:
            break
    else:
        print("a[i] ^ " + str(i) + ':')
        for j in range(len(a)):
            print(chr((a[j] ^ (i)) & 0xff), end='')
        print()