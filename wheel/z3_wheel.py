from z3 import *

# a1 = z3.BitVec("a1", 32)
# a2 = z3.BitVec("a2", 32)
# a3 = z3.BitVec("a3", 32)
# a4 = z3.BitVec("a4", 32)
xorr = [BitVec("num[%d]" % i, 32) for i in range(4)]

s = Solver()

s.add(xorr[0] * 256 - xorr[1] / 2 + xorr[2] * 23 + xorr[3] / 2 == 47118166)
s.add(xorr[0] * 252 - xorr[1] * 366 + xorr[2] * 23 + xorr[3] / 2 - 1987 == 46309775)
s.add(xorr[0] * 6 - xorr[1] * 88 + xorr[2] / 2 + xorr[3] / 2 - 11444 == 1069997)
s.add((xorr[0] - 652) * 2 - xorr[1] * 366 + xorr[2] * 233 + xorr[3] / 2 - 13333 == 13509025)

if s.check() == z3.sat:
    # model = s.model()
    # print(model)
    for i in xorr:
        print(s.model()[i].as_long(), end=",")
