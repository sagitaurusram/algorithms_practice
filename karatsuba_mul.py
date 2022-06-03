def karatsuba_mul(x, y, n):
    if x % 10 == x and y % 10 == y:
        return x * y
    else:
        tenpownby2 = int((10 ** (n / 2)))
        tenpown = int((10 ** n))
        a = int(x / tenpownby2)
        b = int(x % tenpownby2)
        c = int(y / tenpownby2)
        d = int(y % tenpownby2)
        term1 = karatsuba_mul(a, c, int(n/2))
        term2 = karatsuba_mul(b, d, int(n/2))
        term3 = ((a + b) * (c + d) - term1 - term2)
        return (term1 * tenpown) + term2 + (term3 * tenpownby2)


print(str(karatsuba_mul(8, 9, 1)))
print(str(karatsuba_mul(12, 34, 2)))
print(str(karatsuba_mul(1234, 5678, 4)))
