import random
def print_matrix(n):
    for x in range (0,n):
        for y in range(0,n):
            print(random.randint(0,1), end=' ') # end=' ' for printing on the same line
        print()

n = int(input("Enter integer: "))
print_matrix(n)
