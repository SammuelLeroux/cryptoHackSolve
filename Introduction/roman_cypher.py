def roman_cypher(x, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    sentence = x.upper()

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

for i in range(26):
    print(roman_cypher("GWSUS HIFB CIHGWRS SBXCM", i))