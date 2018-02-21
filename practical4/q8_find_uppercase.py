string = input("Enter string:")

def find_num_uppercase(word):
    if len(word)==0:
        return 0
    else:
        if word[0].isupper():
            return find_num_uppercase(word[1:]) + 1
        else:
            return find_num_uppercase(word[1:])

print(find_num_uppercase(string))
