import subprocess
# 有随机数的话，注意操作系统！！！

a = []

for i in range(16, 0xffff):
    c = 0
    j = i
    while (j):
        c = c + 1
        j = j & (j - 1)
    if (c == 10):
        a.append(i)

flag = ""

for i in a:
    proc = subprocess.Popen(['./zorropub'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out = proc.communicate(('1\n%s\n' % i).encode('utf-8'))[0]
    # print(out)
    if "nullcon".encode('utf-8') in out:
        print(out)
        break
