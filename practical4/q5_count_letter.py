def count_letter(str,ch):
    if len(str) == 0:
        return 0
    else:
        return (str[0] == ch) + count_letter(str[1:],ch)

string = input("Enter string: ")
letter = input("Enter letter: ")
print (count_letter(string,letter))
