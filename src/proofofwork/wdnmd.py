from pwn import *
from hashlib import *

s = remote('10.214.24.188',2019)

s.recvuntil("sha384(str).hexdigest()[-6:] == ")
target = s.recvuntil("\n")[:-1]
#print target
i=0
while True:
	if sha384(str(i)).hexdigest()[-6:] == target:
		s.sendlineafter(":",str(i))
		break
	i+=1
s.interactive()