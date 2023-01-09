n = int(input())

def is_sum(a, b, c):
    if (a + b == c or
        a + c == b or 
        b + c == a):
        return 'YES'
    return 'NO' 

for i in range(n):
    inp = input().split()
    print(is_sum(int(inp[0]), int(inp[1]), int(inp[2])))