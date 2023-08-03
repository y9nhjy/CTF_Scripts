import idc

start_addr = 0x7ae580
end_addr = 0x7aeba8
o = [0x33, 0xd2, 0x89, 0x90, 0x94, 0x0c, 0x00, 0x00]
n = [0xc6, 0x80, 0x94, 0x0c, 0x00, 0x00, 0x01, 0x90]
for addr in range(start_addr, end_addr):
    for i in range(len(o)):
        if idc.get_wide_byte(addr + i) != o[i]:
            break
    else:
        for i in range(len(o)):
            ida_bytes.patch_byte(addr, n[i % len(n)])
            addr += 1
        print("[+] Patch Successfully!!!")
