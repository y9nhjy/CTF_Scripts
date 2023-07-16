def fnv_crack(dst):
    for x in range(1 << 32):
        b = x.to_bytes(4, 'little')
        fnv = 0x50C5D1F
        for i in range(4):
            fnv ^= b[i]
            if i == 3:
                break
            fnv = (fnv * 16777619) % (1 << 32)
        if fnv == dst:
            return x
    return None


flag_len = fnv_crack(0x458766D3)  # 134
if flag_len is not None:
    print(flag_len)
