def invert_ascii(x):
    result=""
    for i in x:
        result += chr(i)
    print(result)

arr1 = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
invert_ascii(arr1)
