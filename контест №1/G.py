def rotate(matr):
    new_matr = [[matr[1][0], matr[0][0]], 
                [matr[1][1], matr[0][1]]]
    return new_matr

def is_pretty(matr):
    if (matr[0][1] > matr[0][0] and
        matr[1][1] > matr[1][0] and
        matr[1][0] > matr[0][0] and
        matr[1][1] > matr[0][1]):
        return True
    else:
        return False 

def is_prettible(matr):
    for i in range(4):
        if is_pretty(matr):
            print('YES')
            return 
        else:
            matr = rotate(matr)
    print('NO')

n = int(input())
for i in range(n):
    matr = []
    matr.append(list(map(int, input().split())))
    matr.append(list(map(int, input().split())))
    is_prettible(matr)
