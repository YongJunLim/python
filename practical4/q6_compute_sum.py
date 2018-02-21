def sum_digits(n):
    if n > 0:
        return sum_digits(n // 10) + n % 10
    else:
        return 0

num = int(input("Enter number: "))
print(sum_digits(num))
