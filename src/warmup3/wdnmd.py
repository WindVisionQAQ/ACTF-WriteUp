#import libnum

def LFSR_inv(R,mask):
	str=bin(R)[2:].zfill(208)
	new=str[-1:]+str[:-1]
	new=int(new,2)
	i=(new&mask)&limit
	lsb=0
	while i!=0:
		lsb^=(i&1)
		i=i>>1
	return R>>1 | lsb<<207


flag_ascii = '\x77\x68\x79\x5f\x6c\x66\x35\x72\x5f\x63\x34\x6e\x5f\x62\x33\x5f\x72\x65\x76\x65\x72\x73\x69\x62\x6c\x65'
print flag_ascii
mask = 0x8bc3210d00331741833ca3c4af14f82293653df561b4b55a5a41
key =  0x3a7c0143e3e26d1425b5c3d2d2ae4041de5e22f6557836bdae6f
limit = 0xffffffffffffffffffffffffffffffffffffffffffffffffffff
for _ in range(208):
	key=LFSR_inv(key,mask)
print hex(key)