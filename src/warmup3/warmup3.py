
mask =  0x8bc3210d00331741833ca3c4af14f82293653df561b4b55a5a41
limit = 0xffffffffffffffffffffffffffffffffffffffffffffffffffff

def LFSR(input):
	output = (input << 1) & limit
	i = (input & mask) & limit
	lsb = 0
	while i != 0:
		lsb ^= (i & 1)
		i = i >> 1
	output ^= lsb
	return (output, lsb)

flag = 'ACTF{why_lf5r_c4n_b3_reversible}'
#flag_ascii = '\x77\x68\x79\x5f\x6c\x66\x35\x72\x5f\x63\x34\x6e\x5f\x62\x33\x5f\x72\x65\x76\x65\x72\x73\x69\x62\x6c\x65'
assert len(flag) == 32
R = int(flag[5: -1].encode('hex'), 16)

tmp = 0
for i in range(208):
	(R, lsb) = LFSR(R)
	tmp = (tmp << 1) | lsb
print hex(tmp)
#0x3a7c0143e3e26d1425b5c3d2d2ae4041de5e22f6557836bdae6fL
