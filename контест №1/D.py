l, r = map(int, input().split())


def is_unique(num):
    dig_set = set()
    for dig in str(num):
        if dig in dig_set:
            return False
        else:
            dig_set.add(dig)
    return True

def main():
    for i in range(l, r+1):
        if is_unique(i):
            return i
    return -1


print(main())
