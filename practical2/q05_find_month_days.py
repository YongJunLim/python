year = int(input("Enter year: "))
month = int(input("Enter month: "))

if month == 1:
    print("January {0} has 31 days".format(year))
elif month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("February {0} has 29 days".format(year))
    else:
        print("February {0} has 28 days".format(year))
elif month == 3:
    print("March {0} has 31 days".format(year))
elif month == 4:
    print("April {0} has 30 days".format(year))
elif month == 5:
    print("May {0} has 31 days".format(year))
elif month == 6:
    print("June {0} has 30 days" .format(year))
elif month == 7:
    print("July {0} has 31 days" .format(year))
elif month == 8:
    print("August {0} has 31 days" .format(year))
elif month == 9:
    print("September {0} has 30 days" .format(year))
elif month == 10:
    print("October {0} has 31 days" .format(year))
elif month == 11:
    print("November {0} has 30 days" .format(year))
elif month == 12:
    print("December {0} has 31 days" .format(year))
else:
    print("Please input the correct month.")
