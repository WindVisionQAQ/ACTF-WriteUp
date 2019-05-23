import os


real_flag = 'ACTF{reused_keys_have_slain_Feistel_Cipher|e91bcfd97a}'
fake_flag = 'ACTF{033d4a884dc9389028295ad21617d467071a9845497ce05c}'

def xor(a, b):
	return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

def single_round(m, k):
	assert len(m) == 48
	l = m[: 24]
	r = m[24: ]
	nl, nr = r, xor(k, xor(l, r))
	return nl + nr

def encrypt(m, k):
	for i in k:
		m = single_round(m, i)
	return m



k = []
for i in range(0, 10):
	k.append(os.urandom(24))


#print decrypt(ciphertext.decode('hex'),k)
#print encrypt(real_flag[5: -1], k).encode('hex')
#6f5f5e16d6903a2ad25a67040047bbebd5bcd3f541376852c5380349aa281d1f8bbcd8977a04a88fd4641cb1ac2162e7
#3b001c55d7c8535e8b1d3e004b03eae7d0e787f0403e6a50d331071dfa75133883e691f56a19b6d6bc7416ecf1275b91
cl1='\x6f\x5f\x5e\x16\xd6\x90\x3a\x2a\xd2\x5a\x67\x04\x00\x47\xbb\xeb\xd5\xbc\xd3\xf5\x41\x37\x68\x52'
cr1='\xc5\x38\x03\x49\xaa\x28\x1d\x1f\x8b\xbc\xd8\x97\x7a\x04\xa8\x8f\xd4\x64\x1c\xb1\xac\x21\x62\xe7'
cl2='\x3b\x00\x1c\x55\xd7\xc8\x53\x5e\x8b\x1d\x3e\x00\x4b\x03\xea\xe7\xd0\xe7\x87\xf0\x40\x3e\x6a\x50'
cr2='\xd3\x31\x07\x1d\xfa\x75\x13\x38\x83\xe6\x91\xf5\x6a\x19\xb6\xd6\xbc\x74\x16\xec\xf1\x27\x5b\x91'
pl1='033d4a884dc9389028295ad2'
pr1='1617d467071a9845497ce05c'
pl2=xor(pl1,xor(xor(cl1,cl2),xor(cr1,cr2)))
pr2=xor(pr1,xor(cl1,cl2))
print pl2
print pr2