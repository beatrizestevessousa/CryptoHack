data = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')


for i in range(256):
    flag = ''
    for n in data:
        flag += chr(i ^ n)
    if flag.startswith("crypto"):
        break
    
print(flag)