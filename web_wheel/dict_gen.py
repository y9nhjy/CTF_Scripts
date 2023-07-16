with open('pass.txt', 'w') as f:
    for i in range(100000):
        f.write(str(i) + '\n')
