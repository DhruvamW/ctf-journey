msg='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
msg=bytes.fromhex(msg)

for i in range (0,256):
    result = []
    for b in msg:
        result.append(b ^ i)
    result = bytes(result)
    if b'crypto{' in result:  
        print(result)
