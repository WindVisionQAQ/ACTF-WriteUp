import os
import binascii
import struct

crc32key = 0x3a560186
for i in range(0,65535):
	height = struct.pack('>i',i)
	data = '\x49\x48\x44\x52\x00\x00\x07\x6b'+height+'\x08\x02\x00\x00\x00'
	crc32result = binascii.crc32(data)&0xffffffff
	if crc32result == crc32key:
		print''.join(map(lambda c:"%02x"%ord(c),height))
#misc = open("zhihu.png","rb").read()

#for i in range(1024):
#    data = misc[12:16] + struct.pack('>i',i)+ misc[20:29]
#    crc32 = binascii.crc32(data) & 0xffffffff
#    if crc32 == 0x3a560186:
#        print i
