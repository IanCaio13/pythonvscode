n, n1 = map(int,input().split())
maior = max(n,n1)

menor = min(n,n1)

if maior % menor == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
    