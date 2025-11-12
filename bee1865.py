test_case = int(input())
for k in range (test_case):
    name, strenght = input().split()
    name = str(name)
    strenght = int(strenght)
    if name == 'Thor' or name == 'thor':
        print('Y')
    else:
        print('N')