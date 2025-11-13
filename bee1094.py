n = int(input())
cobacount = 0
coecount = 0
ratcount = 0
sapcount = 0
for k in range (n):
    value, animal = input().split()
    value = int(value)
    animal = str(animal)
    cobacount += value
    if animal == 'C':
        coecount += value
    if animal == 'R':
        ratcount += value
    if animal == 'S':
        sapcount += value
print (f'Total: {cobacount} cobaias')
print (f'Total de coelhos: {coecount}')
print(f'Total de ratos: {ratcount}')
print(f'Total de sapos: {sapcount}')
print(f'Percentual de coelhos: {((coecount/cobacount)*100):.2f} %')
print(f'Percentual de ratos: {((ratcount/cobacount)*100):.2f} %')
print(f'Percentual de sapos: {((sapcount/cobacount)*100):.2f} %')
