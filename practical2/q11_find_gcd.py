n1 = int(input("1st integer: "))
n2 = int(input("2nd integer: "))

d = min(n1, n2)

while d != 0:
    if n1 % d == 0 and n2 % d == 0:
        print(d)

    d -= 1
