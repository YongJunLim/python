def digits_sum(num):
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum

integer = int(input("An integer between 1 and 1000: "))
while integer < 1 or integer > 1000:
    print("Please enter an integer between 1 and 1000")
    integer = int(input("Enter an integer between 1 and 1000: "))

print("The sum of the digits are", digits_sum(integer))