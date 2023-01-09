n = int(input())

def sum_to_count(s):
    if s == 1:
        return 3
    if s == 2:
        return 1
    if s >= 3:
        return 0


for i in range(n):
    game_dict = dict()
    ln = int(input())
    for i in range(3):
        inp = input().split()
        for word in inp:
            if word in game_dict:
                game_dict[word][i] += 1
            else:
                lst = [0,0,0]
                lst[i] += 1
                game_dict[word] = lst

    player_1 = player_2 = player_3 = 0
    counter = [0,0,0]
    for word in game_dict:
        adder = sum_to_count(sum(game_dict[word]))
        if game_dict[word][0] == 1:
            counter[0] += adder
    
        if game_dict[word][1] == 1:
            counter[1] += adder

        if game_dict[word][2] == 1:
            counter[2] += adder
        
    print(counter[0], counter[1], counter[2])
