import idc
st = 0x401910
end = 0x401ED4
ds = "ds:dword_6030CC"

def next_instr(addr):
    return addr + idc.get_item_size(addr)

addr = st
while(addr < end):
    next = next_instr(addr)
    if ds in idc.GetDisasm(addr):
        while(True):
            addr = next
            next = next_instr(addr)
            if "jnz" in idc.GetDisasm(addr):
                dest = idc.get_operand_value(addr, 0)
                ida_bytes.patch_byte(addr, 0xe9)
                ida_bytes.patch_byte(addr+5, 0x90)
                offset = dest - (addr + 5)
                ida_bytes.patch_dword(addr + 1, offset)
                print("patch bcf: 0x%x" % addr)
                addr = next
                break
    else:
        addr = next
print("Successfully!")
