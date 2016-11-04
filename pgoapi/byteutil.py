import ctypes
import struct
from array import array

def asDwordSlice(inp):
    ints = []
    for i in range(0, len(inp)-3, 4):
        ba = bytearray(inp[i:i+4])
        ints.append(ctypes.c_uint32(struct.unpack('<I', array('B', ba))[0]).value)
    return ints
