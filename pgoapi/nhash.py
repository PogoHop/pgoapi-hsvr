import ctypes

HASH_SEED = 0x61247FBF
BLOCK_SIZE = 128

MAGIC_TABLE = [
  0x95C05F4D1512959E, 0xE4F3C46EEF0DCF07,
  0x6238DC228F980AD2, 0x53F3E3BC49607092,
  0x4E7BE7069078D625, 0x1016D709D1AD25FC,
  0x044E89B8AC76E045, 0xE0B684DDA364BFA1,
  0x90C533B835E89E5F, 0x3DAF462A74FA874F,
  0xFEA54965DD3EF5A0, 0x287A5D7CCB31B970,
  0xAE681046800752F8, 0x121C2D6EAF66EC6E,
  0xEE8F8CA7E090FB20, 0xCE1AE25F48FE0A52,
]

MAGIC_ROUND = U128(0x78F32468CD48D6DE, 0x14C983660183C0AE)
MAGIC_FINAL = U128(0xBDB31B10864F3F87, 0x5B7E9E828A9B8ABD)


def hash(inp):
  numBlocks = len(inp) / BLOCK_SIZE
  tailLen = len(inp) & BLOCK_SIZE

  #copy tail, pad with zeroes to multiple of 16
  tail = [0] * 16*((tailLen+15)/16) 
  temptail = inp[len(inp)-tailLen:]
  tail[:len(temptail)] = temptail

  if numBlocks > 0:
    nhash = hashBlock(inp[:BLOCK_SIZE])
  else:
    nhash = hashBlock(tail)

  nhash = addU128(nhash, MAGIC_ROUND)
  if numBlocks > 0:
    for i in range(1, BLOCK_SIZE-1):
      nhash = hashMulAdd(nhash(MAGIC_ROUND), hashBlock(inp[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE]))

    if tailLen > 0:
      nhash = hashMulAdd(nhash, MAGIC_ROUND, hashBlock(tail))

  #Note: 0x7fffffffffffffffffffffffffffffff
  u7fff = (~ctypes.c_uint64(1 << 63).value , ~ctypes.c_uint64(0).value)

  nhash = addU128( nhash, (ctypes.c_uint64(tailLen*8).value, 0) )
  if cmpU128(nhash, u7fff) >= 0:
    nhash = addU128(nhash, (0, 1))
  
def U128(a, b):
  return (ctypes.c_uint64(a).value, ctypes.c_uint64(b).value)

def addU128(a, b):
  res = U128(a[0] + b[0], a[1] + b[1])
  if res[1] < b[1]:
    res[0] ++
  return res

def andU128(a, b):
  return U128(a[0] & b[0], a[1] & b[1])

def mul64_128(a, b):
  return 

def Hash32(buf):
  return Hash32Salt(buf, HASH_SEED)

def Hash32Salt(buf, salt):
  ret = Hash64Salt(buf, salt)
  return ctypes.c_uint32(ret).value ^ ctypes.c_uint32(ret>>32).value

def Hash64(buf):
  return Hash64Salt(buf, HASH_SEED)

def Hash64Salt(buf, salt):
  newBuf = toByteBuffer(ctypes.c_uint32(salt).value) + buf
  return hash(newBuf)

def Hash64Salt64(buf, salt):
  newBuf = toByteBuffer(ctypes.c_uint64(salt).value) + buf
  return hash(newBuf)

def toByteBuffer(inp):
  return str(list(bytearray(struct.pack(">Q", inp))))