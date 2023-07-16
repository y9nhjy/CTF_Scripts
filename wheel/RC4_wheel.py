from arc4 import ARC4
import binascii

key = binascii.unhexlify(b"666c61677b546869735f615f66616b655f666c61677d")
# key = b"you_are_master"
# key = bytearray([121, 109^2, 124^4, 111^6]).decode().encode()
data = binascii.unhexlify(b"A1BFB670635B3BEDF49181A4BD3A53865B8CDB411B73E1D1F2B2DF6E16562242FC")
rc4 = ARC4(key)
ans = rc4.encrypt(data)
print(ans)

# print(binascii.hexlify(ans))
