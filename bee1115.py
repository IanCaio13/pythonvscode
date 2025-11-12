testcase = 1
while testcase != 0:
    coor, coor2 = input().split()
    coor = int(coor)
    coor2 = int(coor2)
    if coor > 0 and coor2 > 0:
        print ('primeiro')
    if coor < 0 and coor2 > 0:
        print ('segundo')
    if coor < 0 and coor2 < 0:
        print('terceiro')
    if coor > 0 and coor2 < 0:
        print('quarto')
    if coor == 0 or coor2 ==0:
        break