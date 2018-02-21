alist = [5, 1, 8, 7, 2]
def find_largest(list):
    if len(list) == 1:
        return list[0]
    else:
        m = find_largest(list[1:])
        return m if m > list[0] else list[0]

print(find_largest(alist))
