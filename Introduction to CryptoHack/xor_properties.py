key1 = int('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313', 16)
key21 = int('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e', 16)
key23 = int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1', 16)
flagWithKeys = int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf', 16)

key2 = key21 ^ key1
key3 = key23 ^ key2
flag = bytes.fromhex(hex(flagWithKeys ^ key1 ^ key2 ^ key3)[2:])

print(flag)
