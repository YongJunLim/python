factors = []
def factor(n):
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors

num = int(input("Integer: "))
factorlist = factor(num)
print("Factors of {} are: {}".format(num, factorlist))
