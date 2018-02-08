def display_pattern(n):

    num = 1
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k+1):
            print(end=" ")
        k = k - 2
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")

n = 5
display_pattern(n)
