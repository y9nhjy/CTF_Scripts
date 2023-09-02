import hashlib


def check(s, md5):
    if hashlib.md5(s).hexdigest() == md5:
        return True
    return False


value = '5a3ebb487ad0046e52db00570339aace'
di = [chr(i) for i in range(0x20, 0x7f)]
lenth = 4
begin = 'Y0uReallyKn0wB4s'
end = ''


def solve(s, idx, lenth):
    if idx == lenth:
        if check((begin + s + end).encode(), value):
            print(begin + s + end)
            exit()
        else:
            return 0

    for i in di:
        solve(s + i, idx + 1, lenth)


solve('', 0, lenth)
