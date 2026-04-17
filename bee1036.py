from math import sqrt
def bee1036():
    a,b,c = map(float,input().split())
    delt = b**2 - (4*a)*c
    if delt >= 0 and a != 0 and b != 0 and c != 0:
        raiz = sqrt(delt)
        x1 = (-b + raiz)/(2*a)
        x2 = (-b - raiz) /(2*a)
        print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}')
    else:
        print('Impossivel Calcular')
          
bee1036()

