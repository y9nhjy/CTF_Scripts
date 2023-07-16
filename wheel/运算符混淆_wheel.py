# (~x|y)-(x|~y)  == x - y
# (~x&y)-(x&~y)  == x - y
# (~x&y)+(x&~y)  == x ^ y
# (~x&y)|(x&~y)  == x ^ y
#  x|y+x|y-x-y   == x ^ y
# ~(~y|~x)|(y^x) == x | y

num = [0, 0, 0, 0, 0, 0, 0]  # +,-,*,/,&,|,^
for i in range(0xff):
    for j in range(1, 0xff):
        x = (i & 0x29 | ~i & 0xd6) ^ (j & 0x29 | ~j & 0xd6)
        if x == i + j:
            num[0] += 1
        if x == i - j:
            num[1] += 1
        if x == i * j:
            num[2] += 1
        if x == i / j:
            num[3] += 1
        if x == i & j:
            num[4] += 1
        if x == i | j:
            num[5] += 1
        if x == i ^ j:
            num[6] += 1
switch = {0: 'a + b', 1: 'a - b', 2: 'a * b', 3: 'a / b', 4: 'a & b', 5: 'a | b', 6: 'a ^ b'}
for i in range(7):
    print(switch[i], ':', num[i])
