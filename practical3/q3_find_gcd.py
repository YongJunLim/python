def gcd(m, n):
    while n:
        m, n = n, m%n
    return m

print(gcd(24,16))
print(gcd(255,25))
