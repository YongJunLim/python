num=0
pos=0
i=0

def is_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

while num<1000:
    i+=1
    if is_prime(i) == True:
        print(i,end="\t")
        pos+=1
        num+=1
    if pos == 10:
        print()
        pos=0
