n = int(input())
for k in range (n):
    n1,n2,n3 = input().split()
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    mult = (n1*2+n2*3+n3*5)/(2+3+5)
    print (f'{mult:.1f}')
