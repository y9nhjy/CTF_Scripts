import xxtea
import xtea
import binascii

# s:密文  key:密钥(16字节)
s = 0x9577b998e8d2960c1becc680f6004a581ea68ab15b4278b3feb44972d1c43ac537e09aff5062cc0c90026e1c
s = s.to_bytes(len(hex(s)[2:]) // 2, 'big')
# 如果密钥是{0x1234,0x2345,0x4567,0x6789}
# 则key = 0x34120000452300006745000089670000.to_bytes(16, 'big')
key = b'FMT2ZCEHS6pcfD2R'
flag = xxtea.decrypt(s, key, padding=False)
print(flag)
# i = int.from_bytes(flag, 'big')
# print(hex(i))
# flag=binascii.unhexlify(flag)


# 字符串转32位数组 小端序
s = '44583339303600000000000000000000646F63746F7233000000000000000000'
for i in range(int(len(s) / 8)):
    print(",0x"+s[i*8+6:i*8+8]+s[i*8+4:i*8+6]+s[i*8+2:i*8+4]+s[i*8:i*8+2], end='')

# 32位大小端互换
s = '150E0700312A231C4D463F3869625B54857'
for i in range(int(len(s)/8)):
    print(s[i*8+6:i*8+8]+s[i*8+4:i*8+6]+s[i*8+2:i*8+4]+s[i*8:i*8+2],end='')
