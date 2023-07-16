import dis
import marshal

# conda activate py3.11
# cd D:\Ctf\Ctf\wheel
# D:
# python ./pyc字节码.py
with open('D:/Ctf/pyinstxtractor-master/game.exe_extracted/game.pyc', 'rb') as f:
    f.seek(16)
    code = marshal.load(f)
    with open('pyc.txt', 'w') as f:
        dis.dis(code, file=f)
