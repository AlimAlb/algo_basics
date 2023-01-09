def signs(s, l):
    sign_flag = None
    if s[0] == '1':
        sign_flag = True
    else:
        sign_flag = False
    out_s = ''
    for i in range(1, l):
        if s[i] == '1':
            out_s += '-' if sign_flag else '+'
            sign_flag = not(sign_flag)
        if s[i] == '0':
            out_s += '+'
    return out_s

n = int(input())
for i in range(n):
    l = int(input())
    s = input()
    print(signs(s, l))    
