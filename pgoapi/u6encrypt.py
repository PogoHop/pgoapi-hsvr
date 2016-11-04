import struct


from u6encryptalgo import sub_9E9D8
from byteutil import asDwordSlice

def crand(val):
    val = (0x41C64E6D * val) + 0x3039
    return (val, byte(val >> 16, 0))

def byte(number, i):
    return (number & (0xff << (i * 8))) >> (i * 8)

def toByteList(inp):
    return list(bytearray(struct.pack(">I", inp)))

def makeIntegrityByte(rand):
    lastbyte = crand(rand)[1]
    v74 = (lastbyte ^ 0x0C) & lastbyte
    v75 = ((~v74 & 0x67) | (v74 & 0x98)) ^0x6F | (v74 & 8)
    return int(v75)

def encryptU6(inp, msSinceStart):
    #print "INPUT:"
    #print inp
    #print msSinceStart

    rand = msSinceStart
    iv = [0] * 256
    for i in range(256):
        cr = crand(rand)
        rand = cr[0]
        iv[i] = cr[1]

    arr3 = [0] * 256

    ivBlock = iv
    inputlen = len(inp)
    blockcount = (inputlen + 256) / 256
    roundedsize = blockcount * 256
    totalsize = roundedsize + 4

    output = [0] * totalsize 
    output[:3] = toByteList(msSinceStart)
    output[4:4+len(inp)] = inp

    output[totalsize-1] = byte(roundedsize - inputlen, 0)

    for offset in range(4, totalsize, 256):
        for i in range(256):
            output[offset+i] ^= ivBlock[i]

        arr3 = sub_9E9D8(asDwordSlice(output[offset:offset+256]), asDwordSlice(arr3))

        ivBlock[:len(arr3)] = arr3
        output[offset:offset+len(arr3)] = arr3

    output[totalsize] = makeIntegrityByte(rand)

    #print "OUTPUT:"
    #print output

    return output