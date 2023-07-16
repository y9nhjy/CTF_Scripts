import binascii


def b58decode(tmp: str) -> str:
    base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    temp = []
    for i in tmp:
        temp.append(base58.index(i))
    tmp = temp[0]
    for i in range(len(temp) - 1):
        tmp = tmp * 58 + temp[i + 1]
    return binascii.unhexlify(hex(tmp)[2:].encode("utf-8")).decode("UTF-8")


print(b58decode("9pd5duAv9fueatCwqEwuy7"))
# GoM0bi13G3tItEzF
