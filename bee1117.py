test_case = 1
nval = 0
sum = 0
while test_case != 0:
    n = float(input())
    if n < 0 or n > 10:
        print('nota invalida')
    if n >= 0 and n <= 10:
        sum += n
        nval += 1
    if nval == 2:
        break
print(f'media = {sum/2}')
    