n = int(input("Enter milliseconds: "))

def convert_ms(n):
    rawSecond = n // 1000
    second = rawSecond % 60
    rawMinute = rawSecond // 60
    minute = rawMinute % 60
    hour = rawMinute // 60
    print("{0}:{1}:{2}".format(hour,minute,second))

convert_ms(n)
