def XOR_word(word, key):
    def XOR(x,y):
        result = ""
        for i in range(len(x)):
            if x[i] == y[i]:
                result += "0"
            else:
                result += "1"
        return result

    def autocomp(x):
        result = ""
        new_x = str(x[2:])
        if (len(new_x) < 4):
            for i in range((4 - len(str(new_x)))):
                result += "0"
        return result + new_x

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    tab_result=[]
    for i in range(len(word)):
        for j in range(len(alphabet)):
            if word[i] == alphabet[j]:
                tab_result.append(str(XOR(autocomp(bin(j + 1)), bin(key)[2:])))

    result = ""
    for i in range(len(tab_result)):
        for j in range(len(alphabet)):
            if j == int(tab_result[i], 2):
                result += alphabet[j - 1]

    print("crypto{" + result + "}")
    return 1

#XOR_word("label", 13)