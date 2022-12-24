def euclid(a, b):
    print(f'euclid({a}, {b})')
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

# a = 21
# b = 9
# a = 1597
# b = 2584
a = 1134903170
b = 1836311903
print(f'gcd of {a} and {b}: {euclid(a, b)}')