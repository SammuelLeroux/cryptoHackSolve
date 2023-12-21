def quad_resid(sq_a, p):
    for i in range(p):
        if i**2 % p == sq_a:
            print(i)
            return 1
    print(sq_a)

# quad_resid(14, 29)
# quad_resid(6, 29)
# quad_resid(11, 29)