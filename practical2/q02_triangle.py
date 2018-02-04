def valid():
    if p - a <= a:
        return False
    elif p - b <= b:
        return False
    elif p - c <= c:
        return False
    else:
        return True

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

p = a + b + c


if valid():
    print("Perimeter = ", p)
else:
    print("Invalid triangle!")
