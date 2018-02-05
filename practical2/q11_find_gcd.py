n1 = int(input("1st integer: "))
n2 = int(input("2nd integer: "))
d = min(n1,n2)

def gcd(d,n1,n2):
    if n1 % d == 0 and n2 % d == 0:
        return d
    else:
        return gcd(d-1,n1,n2)

print(gcd(d,n1,n2))
