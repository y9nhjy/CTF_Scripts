import idc
start_addr = 0x406300
end_addr = 0x406E14
l = [0x74, 0x15, 0x75, 0x13]
for addr in range(start_addr, end_addr):
    for i in range(len(l)):
        if idc.get_wide_byte(addr + i) != l[i]:
            break
    else:
        for i in range(19):
            ida_bytes.patch_byte(addr + i + 4, 0x90)
        print("[+] nop ok!!")

