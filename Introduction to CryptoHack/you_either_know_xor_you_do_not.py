string = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
starting = b"crypto{"
key = []

for (list1, list2) in zip(string, starting):
    key.append(list1 ^ list2)
key.append(ord('y'))

numbers = []
key_len = len(key)
for i in range(len(string)):
    numbers.append(string[i] ^ key[i % key_len])
 
flag = ''
for n in numbers:
    flag += chr(n)
    
print(flag)
