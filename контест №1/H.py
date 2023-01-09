iters = int(input())

for i in range(iters):
    n = int(input())
    s = str(n)
    ln = len(s)
    print((len(s)-1)*9 + int(s[0])) 
