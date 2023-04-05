import email.utils
import sys
import re

pattern = r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.([a-zA-Z]{1,3})$'

n = int(sys.stdin.readline())

lst = []
for i in range(0, n):
    addr = sys.stdin.readline()
    parse_addr = email.utils.parseaddr(addr)
    
    if  re.match(pattern, parse_addr[1]):
        lst.append(parse_addr)
    

for i in range(len(lst)):
    print(email.utils.formataddr(lst[i]))
    
    
    