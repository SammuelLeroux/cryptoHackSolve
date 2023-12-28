def XOR_prop():

    def hex_to_bytes(hex_string):
        return bytes.fromhex(hex_string)
    
    def xor(x, y):
        return bytes(a ^ b for a, b in zip(x, y))
    
    k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
    k2_1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
    k2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
    f_k1_3_2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

    xor_k1 = hex_to_bytes(k1)
    xor__k2_1 = hex_to_bytes(k2_1)
    xor_k2_3 = hex_to_bytes(k2_3)
    xor_f_k1_3_2 = hex_to_bytes(f_k1_3_2)

    flag = xor(xor(xor_f_k1_3_2, xor_k2_3), xor_k1)

    print(flag)
    
    return 1

XOR_prop()