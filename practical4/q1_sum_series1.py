n = int(input("Enter integer: "))

def sum_series1(i):
    if i == 1:
        return 1
    else:
        return sum_series1(i-1) + 1/i

print(sum_series1(n))
