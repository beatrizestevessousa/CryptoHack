string = 'label'
flag = ''

for letter in string:
    num = ord(letter)
    compared = num ^ 13
    new_letter = chr(compared)
    flag += new_letter
    
print(flag)
