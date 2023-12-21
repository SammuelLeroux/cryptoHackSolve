def roman_emperor_cypher(x):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    sentence = x.upper()

    for key in range(26):
        result = ""
        for i in range(len(sentence)):
            if sentence[i] in alphabet:
                for j in range(len(alphabet)):
                    if sentence[i] == alphabet[j]:
                        index = (j + key) % 26
                        if x[i] == sentence[i]:
                            result += alphabet[index]
                        else:
                            result += alphabet[index].lower()
            else:
                result += sentence[i]
        print(result)

    return 1

# to_dec = "GWSUS HIFB CIHGWRS SBXCM"
# roman_emperor_cypher(to_dec)