import hashlib


def check(s, md5):
    if hashlib.md5(s).hexdigest() == md5:
        return True
    return False


md = '5a3ebb487ad0046e52db00570339aace'
di = [chr(i) for i in range(0x20, 0x7f)]
len = 4
begin = 'Y0uReallyKn0wB4s'
end = ''
# md = 'c8837b23ff8aaa8a2dde915473ce0991'
# di = '0123456789'
# len = 6
# begin = ''
# end = ''


def solve(s, idx, totallenth):
    if idx == totallenth:
        if check((begin + s + end).encode(), md):
            print(begin + s + end)
            exit()
        else:
            return 0

    for i in di:
        solve(s + i, idx + 1, totallenth)


solve('', 0, len)
