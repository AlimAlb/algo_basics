iters = int(input())

def count(n, k):
    counter = 0
    while n > 0:
        if n % k == 0:
            n = n // k
            counter += 1
        else:
            counter += n % k
            n -= n % k

    return counter


for i in range(iters):
    n, k = map(int, input().split())
    print(count(n, k))

