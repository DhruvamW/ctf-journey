key1='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key1= bytes.fromhex(key1)
key1=int(''.join(format(byte, '08b') for byte in key1),2)
##print(key1)

key1_xor_key2= '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key1_xor_key2= bytes.fromhex(key1_xor_key2)
key1_xor_key2=int(''.join(format(byte, '08b') for byte in key1_xor_key2),2)
##print(key1_xor_key2)

key2_xor_key3='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
key2_xor_key3= bytes.fromhex(key2_xor_key3)
key2_xor_key3=int(''.join(format(byte, '08b') for byte in key2_xor_key3),2)
##print(key2_xor_key3)

flag_xor_key_xor_key2_xor_key3='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
flag_xor_key_xor_key2_xor_key3= bytes.fromhex(flag_xor_key_xor_key2_xor_key3)
flag_xor_key_xor_key2_xor_key3=int(''.join(format(byte, '08b') for byte in flag_xor_key_xor_key2_xor_key3),2)
##print(flag_xor_key_xor_key2_xor_key3)

key1_xor_key3= key1_xor_key2 ^ key2_xor_key3
##print(key1_xor_key3)

flag_xor_key2= flag_xor_key_xor_key2_xor_key3 ^ key1_xor_key3
##print(flag_xor_key2)

key2= key1_xor_key2 ^ key1
##print(key2)

flag = flag_xor_key2 ^ key2
print(flag)
print(hex(flag))
print(bytes.fromhex(hex(flag)[2:]))
