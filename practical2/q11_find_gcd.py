n1 = int(input("1st integer: "))
n2 = int(input("2nd integer: "))

def gcd(m, n):
    while n:
        m, n = n, m%n
    return m

print(gcd(n1,n2))
