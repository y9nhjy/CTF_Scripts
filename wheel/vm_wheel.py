opcode = [80, 3, 3, 0, 29, 1, 1, 3, 80, 3, 3, 1, 29, 1, 2, 3, 29, 3, 6, 1, 113, 1, 2, 80, 2, 3, 1, 80, 2, 5, 2, 114, 2,
          31, 41, 1, 2, 80, 3, 4, 32, 150, 2, 4, 2, 116, 3, 4, 87, 1, 3, 80, 2, 2, 6, 220, 3, 2, 2, 80, 1, 3, 2, 29, 2,
          1, 3, 80, 2, 2, 5, 113, 2, 1, 80, 2, 3, 2, 80, 2, 4, 1, 114, 4, 31, 41, 2, 4, 80, 3, 5, 32, 150, 2, 5, 4, 116,
          3, 5, 87, 2, 3, 80, 2, 3, 6, 220, 3, 3, 2, 29, 3, 3, 1, 80, 1, 4, 3, 29, 2, 2, 4, 7, 153, 255]
reg_table = {
    '1': 'EAX',
    '2': 'EBX',
    '3': 'ECX',
    '4': 'EDX',
    '5': 'R8',
    '6': 'CNT',
    '7': 'EIP'}

i = 0
while i < len(opcode):
    if opcode[i] == 80:
        if opcode[i + 1] == 0x1:
            print(f"{reg_table[str(opcode[i + 2])]} = extendKey[{reg_table[str(opcode[i + 3])]}]")
        elif opcode[i + 1] == 0x2:
            print(f"{reg_table[str(opcode[i + 2])]} = {reg_table[str(opcode[i + 3])]}")
        elif opcode[i + 1] == 0x3:
            print(f"{reg_table[str(opcode[i + 2])]} = {str(opcode[i + 3])}")
        i += 4
    elif opcode[i] == 29:
        if opcode[i + 1] == 0x1:
            print(f"{reg_table[str(opcode[i + 2])]} += extendKey[{reg_table[str(opcode[i + 3])]}]")
        elif opcode[i + 1] == 0x2:
            print(f"{reg_table[str(opcode[i + 2])]} += {reg_table[str(opcode[i + 3])]}")
        elif opcode[i + 1] == 0x3:
            print(f"{reg_table[str(opcode[i + 2])]} += {str(opcode[i + 3])}")
        i += 4
    elif opcode[i] == 113:
        print(f"{reg_table[str(opcode[i + 1])]} ^= {reg_table[str(opcode[i + 2])]}")
        i += 3
    elif opcode[i] == 114:
        print(f"{reg_table[str(opcode[i + 1])]} &= {str(opcode[i + 2])}")
        i += 3
    elif opcode[i] == 150:
        if opcode[i + 1] == 0x1:
            print(f"{reg_table[str(opcode[i + 2])]} -= extendKey[{reg_table[str(opcode[i + 3])]}]")
        elif opcode[i + 1] == 0x2:
            print(f"{reg_table[str(opcode[i + 2])]} -= {reg_table[str(opcode[i + 3])]}")
        elif opcode[i + 1] == 0x3:
            print(f"{reg_table[str(opcode[i + 2])]} -= {str(opcode[i + 3])}")
        i += 4
    elif opcode[i] == 87:
        print(f"{reg_table[str(opcode[i + 1])]} |= {reg_table[str(opcode[i + 2])]}")
        i += 3
    elif opcode[i] == 116:
        print(f"{reg_table[str(opcode[i + 1])]} >>= {reg_table[str(opcode[i + 2])]}")
        i += 3
    elif opcode[i] == 41:
        print(f"{reg_table[str(opcode[i + 1])]} <<= {reg_table[str(opcode[i + 2])]}")
        i += 3
    elif opcode[i] == 220:
        if opcode[i + 1] == 0x1:
            print(f"{reg_table[str(opcode[i + 2])]} *= extendKey[{reg_table[str(opcode[i + 3])]}]")
        elif opcode[i + 1] == 0x2:
            print(f"{reg_table[str(opcode[i + 2])]} *= {reg_table[str(opcode[i + 3])]}")
        elif opcode[i + 1] == 0x3:
            print(f"{reg_table[str(opcode[i + 2])]} *= {str(opcode[i + 3])}")
        i += 4
    elif opcode[i] == 7:
        print("R8 = CNT == 21")
        i += 1
    elif opcode[i] == 153:
        print("JMP HEAD IF R8")
        i += 2
