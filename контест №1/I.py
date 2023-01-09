import math

iters = int(input())
def count(num):

    i = 2
    pow2 = set()
    pow3 = set()
    while i < int((num)**(1/2)+1):

        if i**3 <= num:
            pow3.add(i**3)
        if i**2 <= num and not(i**2 in pow3):
            pow2.add(i**2)
        
            
        i += 1

    print(1 + len(pow2) + len(pow3))
    
for i in range(iters):
    num = int(input())
    count(num)
#4 9 16 25
#8 
#1