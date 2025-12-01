n = float(input())
if n < 2000:
    print('Isento')
elif n > 2000.01 and n <= 3000:
    print(f'R$ {(n - 2000)*8/100:.2f}')
elif n > 3000.01 and n <= 4500:
    print(f'R$ {((n - 3000) * 18/100)+80:.2f}' )
elif n > 4500.01:
    print(f'R$ {(n - 4500)*(28/100)+80+270:.2f}' )