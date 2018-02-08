def m_series(i):
    value = 0
    for i in range(1,i+1):
        value += i/(i+1)
    return value



print("i","m_series(i)")

for i in range(1, 21):
    print("{0}\t{1:.4f}".format(i, m_series(i)))
