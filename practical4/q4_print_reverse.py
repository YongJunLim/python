def reverseString(x):
    if x == "":
        return ""
    else:
        return x[::-1]

num = input("Enter number: ")
print(reverseString(num))
