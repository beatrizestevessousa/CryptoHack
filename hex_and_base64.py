import base64

hexa = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

decoded = bytes.fromhex(hexa)

flag = base64.b64encode(decoded)

print(flag)
