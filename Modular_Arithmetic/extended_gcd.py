def extended_gcd(p, q):
    if q == 0:
        return (p, 1, 0)
    else:
        g, u, v = extended_gcd(q, p % q)
        return (g, v, u - (p // q) * v)

def bezout_coefficients(p, q):
    g, u, v = extended_gcd(p, q)
    return u, v

# Example usage:
p = 26513
q = 32321

u, v = bezout_coefficients(p, q)

# print(f"Bézout coefficients for {p} and {q}: u = {u}, v = {v}")
# print(f"{p} * {u} + {q} * {v} = {p * u + q * v}")

# print(min(u, v))