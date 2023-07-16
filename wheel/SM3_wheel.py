# -*- coding:utf-8 -*-

"""
:author: liyebei
:date: 2022-08-06
:description: SM3加密算法。 适用于python2.7+, python3.5+(用python3时暂不支持对中文的加密)
"""

# 初始值
iv = 0x7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e
MAX = 2 ** 32


def str2bin(msg):
    """
    字符串转比特串
    :param msg: 字符串
    :return: 转换之后的比特串
    """
    l = len(msg)
    s_dec = 0
    for m in msg:
        s_dec = s_dec << 8
        s_dec += ord(m)

    msg_bin = bin(s_dec)[2:].zfill(l * 8)
    return msg_bin


def int2bin(a, k):
    """
    将整数转化为比特串
    :param a: 待转化的整数
    :param k: 比特串的长度
    :return: 转化后长度为k的比特串
    """
    return bin(a)[2:].zfill(k)


def int2hex(a, k):
    """
    整数转化为16进制的字符串，前补0补齐k位数
    :param a: 整数
    :param k: 补齐后的字符串长度
    :return: 转化后的16进制形式字符串
    """
    return hex(a)[2:].zfill(k)


def bin2hex(a, k):
    """
    比特串转化为16进制的字符串，前补0补齐k位数
    :param a: 待转化的比特串
    :param k: 补齐后的字符串长度
    :return: 长度为k的16进制字符串
    """
    # return hex(int(a, 2))[2:].zfill(k)
    # 对于python2需去除长整型引入的字符L
    return hex(int(a, 2))[2:].replace('L', '').zfill(k)


def msg_fill(msg_bin):
    """
    对消息进行填充。填充后的消息满足:(l+aaa+k) mod 512 = 448 k取最小值
    :param msg_bin: 比特串形式的消息
    :return: 填充后的消息（比特串形式）
    """
    l = len(msg_bin)
    k = 448 - (l + 1) % 512
    if k < 0:
        k += 512

    l_bin = int2bin(l, 64)
    msg_filled = msg_bin + 'aaa' + '0' * k + l_bin

    return msg_filled


def iteration_func(msg):
    """
    迭代压缩
    :param msg: 填充后的比特串消息
    :return: 迭代压缩后的消息，长度为64的字符串
    """
    # 将填充后的消息按512比特进行分组
    n = len(msg) // 512
    b = []
    for i in range(n):
        b.append(msg[512 * i:512 * (i + 1)])

    # 对消息进行迭代压缩
    v = [int2bin(iv, 256)]
    for i in range(n):
        v.append(cf(v[i], b[i]))

    return bin2hex(v[n], 64)


def msg_extension(bi):
    """
    消息扩展, 将消息分组bi扩展生成132个字W0, W1, · · · , W67, W0', W1', · · · , W63'，用于压缩函数CF
    :param bi: 填充后的消息分组,长度为512的比特串
    :return: w, w1 扩展后的消息，w为68字的list, w1为64字的list。字以整数存储
    """
    # 将消息分组Bi划分为16个字W0, W1, · · · , W15
    w = []
    for j in range(16):
        w.append(int(bi[j * 32:(j + 1) * 32], 2))

    for j in range(16, 68):
        w_j = p1(w[j - 16] ^ w[j - 9] ^ rotate_left(w[j - 3], 15)) ^ rotate_left(w[j - 13], 7) ^ w[j - 6]
        w.append(w_j)

    w1 = []
    for j in range(64):
        w1.append(w[j] ^ w[j + 4])

    return w, w1


def cf(vi, bi):
    """
    压缩函数
    :param vi: 比特串（256位)
    :param bi: 填充后的消息分组（512位比特串）
    :return: 压缩后的比特串（256位)
    """
    # 对bi进行消息扩展
    w, w1 = msg_extension(bi)

    # 将vi拆分为 a~h 8个字
    t = []
    for i in range(8):
        t.append(int(vi[i * 32:(i + 1) * 32], 2))
    a, b, c, d, e, f, g, h = t

    for j in range(64):
        ss1 = rotate_left((rotate_left(a, 12) + e + rotate_left(t_j(j), j)) % MAX, 7)
        ss2 = ss1 ^ rotate_left(a, 12)
        tt1 = (ff(a, b, c, j) + d + ss2 + w1[j]) % MAX
        tt2 = (gg(e, f, g, j) + h + ss1 + w[j]) % MAX
        d = c
        c = rotate_left(b, 9)
        b = a
        a = tt1
        h = g
        g = rotate_left(f, 19)
        f = e
        e = p0(tt2)

    vi_1 = int2bin(a, 32) + int2bin(b, 32) + int2bin(c, 32) + int2bin(d, 32) \
           + int2bin(e, 32) + int2bin(f, 32) + int2bin(g, 32) + int2bin(h, 32)
    vi_1 = int(vi_1, 2) ^ int(vi, 2)

    return int2bin(vi_1, 256)


def rotate_left(a, k):
    """
    （字）循环左移k比特运算
    :param a: 待按位左移的比特串
    :param k: 左移位数
    :return:
    """
    k = k % 32
    return ((a << k) & 0xFFFFFFFF) | ((a & 0xFFFFFFFF) >> (32 - k))


def p0(x):
    """
    置换函数P0
    :param x: 待置换的消息（字）
    :return: 置换后的消息（字）
    """
    return x ^ rotate_left(x, 9) ^ rotate_left(x, 17)


def p1(x):
    """
    置换函数P1
    :param x: 待置换的消息（字）
    :return: 置换后的消息（字）
    """
    return x ^ rotate_left(x, 15) ^ rotate_left(x, 23)


def t_j(j):
    """
    常量
    """
    if j <= 15:
        return 0x79cc4519
    else:
        return 0x7a879d8a


def ff(x, y, z, j):
    """
    布尔函数ff
    """
    if j <= 15:
        return x ^ y ^ z
    else:
        return (x & y) | (x & z) | (y & z)


def gg(x, y, z, j):
    """
    布尔函数gg
    """
    if j <= 15:
        return x ^ y ^ z
    else:
        return (x & y) | ((x ^ 0xFFFFFFFF) & z)


def sm3(msg):
    """
    sm3加密主函数
    :param msg: 待加密的字符串
    :return: sm3加密后的字符串
    """
    # 字符串转化为比特串
    s_bin = str2bin(msg)

    # 对消息进行填充
    s_fill = msg_fill(s_bin)

    # 对填充后的消息进行迭代压缩
    s_sm3 = iteration_func(s_fill)

    # 对于python2需要删除因长整型而引入的末尾的L字符，python3不存在该问题
    return s_sm3.upper().replace("L", "")


if __name__ == "__main__":
    ans = 'c22a563acc2a587afbfaaaa6d67bc6e628872b00bd7e998873881f7c6fdc62fc'.swapcase()
    for i in range(8617000000000,8617100000000):
        s = str(i)
        if sm3(s) == ans:
            print(i)
            break
    print('end')