def mod_invert(g, m):
    for d in range(m):
        if (g * d) % m == 1:
            if d / g == d // g:
                print(d)
                return 1
    return 0

# mod_invert(3, 13)
            
