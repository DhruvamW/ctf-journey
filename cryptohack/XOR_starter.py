msg="label"
arr=""
for i in msg:
    i=ord(i)^13
    print(i)
    i=chr(i)
    print(i)
    arr+=str(i)
print(arr)