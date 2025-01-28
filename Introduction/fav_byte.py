def fav_byte():
    x = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    z = bytes.fromhex(x)

    def xor(data, key):
        return bytes(byte ^ key for byte in data)

    for i in range(256):
        result = xor(z, i)
        # Affiche uniquement les résultats plausibles
        if all(32 <= b <= 126 for b in result):  # ASCII-readable check
            print(f"Key: {i}, Message: {result}")

    return 1

fav_byte()