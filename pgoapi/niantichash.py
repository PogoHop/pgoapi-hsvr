import ctypes
import socket
import struct
from array import array

#from unicorn import *
#from unicorn.arm_const import *

HASH_SEED = ctypes.c_int32(0x61247FBF).value
CODE_ADDR = ctypes.c_int64(0x1000).value

TCP_IP = '127.0.0.1'
TCP_PORT = 1500

class NianticHash:
    def __init__(self):
        """
        self.mu = Uc(UC_ARCH_ARM, UC_MODE_THUMB)

        #Map heap and stack.
        self.createMap(0xE0000000, 0x2000)
        self.createMap(0xD0000000, 0x2000)
        sp = 0xD0000000 + 0x1000
        self.mu.reg_write(UC_ARM_REG_SP, ctypes.c_int64(sp).value)

        #Code segment with call to hash function.
        self.createMap(CODE_ADDR, 0x1000)
        self.memMap(CODE_ADDR, b"\x90\x47")

        self.mu.hook_add(UC_HOOK_CODE, self.unicornCodeHook)

        #iOS specific, pokemongo32 should be the first 0x02C9C5A0 bytes of the binary (32-bit area only)
        buf = open("pokemongo", "rb").read() 

        self.createMap(0x98C0, 0x03228D58 - 0x000098C0)
        self.memMap(0x98C0, buf[0x98C0:0x03228D58 - 0x98C0])
        self.memMap(0x01BE9D9E, b"\x00\x20")

        exportaddr = 0x2C84000
        for i in range(0x1098B):
            value = ctypes.c_int32(struct.unpack('<I', array('B', buf[exportaddr+i*4:exportaddr+i*4+4]))[0]).value

            if value == 0:
                self.memMap(ctypes.c_int64(exportaddr+(i*4)).value, b"\xD0\x70\x0E\x03")

        print "QEMU init successful."
        """

    def unicornCodeHook(mu, addr, size):
        pass

    def createMap(self, addr, size):
        chunk = addr % 0x1000
        taddr = addr - chunk
        tsize = ((0xFFF + chunk + size) / 0x1000) * 0x1000
        self.mu.mem_map(taddr, tsize)

    def memMap(self, address, buf):
        self.mu.mem_write(address, str(buf))


    def hash(self, buf):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP,TCP_PORT))
        #s.send(b"\x61\x24\x7f\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
        #print "sending:"
        #print list(bytearray(buf))
        s.send(buf)
        data = s.recv(8)
        num = struct.unpack('<Q', data)
        #print "HASH: " + str(hex(num[0]))
        return num[0]
        """
        self.mu.reg_write(UC_ARM_REG_R0, 0xE0001000) # buffer
        self.mu.reg_write(UC_ARM_REG_R1, ctypes.c_int64(len(buf)).value) # size
        self.mu.reg_write(UC_ARM_REG_R2, 0x01BE8290+1) # hash function address

        self.memMap(0xE0001000, buf)

        self.mu.emu_start(CODE_ADDR, CODE_ADDR+2)

        r0 = self.mu.reg_read(UC_ARM_REG_R0)
        r1 = self.mu.reg_read(UC_ARM_REG_R1)
        return r1<<32 | r0&0xFFFFFFFF
        """

    def Hash32(self, buf):
        return self.Hash32Salt(buf, HASH_SEED)

    def Hash32Salt(self, buf, salt):
        ret = self.Hash64Salt(buf, salt)
        return ctypes.c_uint32(ret).value ^ ctypes.c_uint32(ret>>32).value

    def Hash64(self, buf):
        return self.Hash64Salt(buf, HASH_SEED)

    def Hash64Salt(self, buf, salt):
        newBuf = self.toByteList(ctypes.c_uint32(salt).value) + buf
        return self.hash(newBuf)

    def Hash64Salt64(self, buf, salt):
        newBuf = self.toByteList(ctypes.c_uint64(salt).value) + buf
        return self.hash(newBuf)

    def toByteList(self, inp):
        return str(list(bytearray(struct.pack(">Q", inp))))
