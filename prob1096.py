i = 1
j = 8
while i < 9:
    for k in range(15):
        if k == 3:
            i = 3
        if k == 6:
            i = 5
        if k == 9:
            i = 7
        if k == 12:
            i = 9
        j-=1
        if j < 5:
            j = 7
        print(f'I={i} J={j}')
        