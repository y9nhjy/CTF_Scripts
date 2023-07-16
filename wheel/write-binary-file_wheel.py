with open('gamemessage', 'rb') as f:
    with open('gamemessage_2', 'wb') as f_2:
        b = f.read()
        for i in range(len(b)):
            f_2.write((b[i] ^ 34).to_bytes(1, 'little'))
