from math import factorial
while True:
    try:
        m,n = map(int,input().split())
        fac = factorial(m)
        fac2 = factorial(n)
        print(fac+fac2)
    except EOFError:
        break
