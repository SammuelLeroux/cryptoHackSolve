def gcd(a, b):
    def decomp(x):
        result = []
        for i in range(1, x):
            if x % i == 0:
                result.append(i)
        return result

    decomp_a = decomp(a)
    decomp_b = decomp(b)

    tab_gcd = []
    for elem in decomp_a:
        if elem in decomp_b:
            tab_gcd.append(elem)

    print(max(tab_gcd))
    return 1


# gcd(12, 8)
# gcd(66528, 52920)