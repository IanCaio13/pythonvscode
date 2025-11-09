#num = int(input())
#while num != 0:
#    digite = int(input)
num = int(input())
for k in range(num):
    digite = int(input())
    if digite % 2 == 0 and digite > 0:
        print('EVEN POSITIVE')
    if digite % 2 == 0 and digite < 0:
        print('EVEN NEGATIVE')
    if digite % 2 != 0 and digite > 0:
        print('ODD POSITIVE')
    if digite % 2 != 0 and digite < 0:
        print('ODD NEGATIVE')
    if  digite == 0:
        print('NULL')
