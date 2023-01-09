s = input()


def count_qaqs(s):
    Qs_pre = 0
    Qs_post = s.count("Q")
    counter = 0
    for sym in s:
        if sym == 'Q':
            Qs_post -= 1
            Qs_pre += 1
        if sym == 'A':
            counter += Qs_post*Qs_pre
    return counter

print(count_qaqs(s))

    
    