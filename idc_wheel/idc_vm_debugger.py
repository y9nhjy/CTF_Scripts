# 下断点，右键断点 Edit breakpoint
op_addr = 0xbf4018
ebp = idc.get_reg_value('ebp')
p0 = ida_bytes.get_word(ebp - 0xC)
p1 = ida_bytes.get_word(ebp - 0x8)
p2 = ida_bytes.get_word(ebp - 0x10)
op_p0 = ida_bytes.get_word(op_addr + p0 * 2)
op_p1 = ida_bytes.get_word(op_addr + p1 * 2)
print('op[%d] = ~(op[%d] & op[%d]) ' % (p2, p0, p1), '(op[%d] = ~(%d & %d))' % (p2, op_p0, op_p1))


ebp = idc.get_reg_value('ebp')
v4 = ida_bytes.get_word(ebp - 0x24)
if (v4 == 36):
    print('----------------------------END INPUT------------------------------')
