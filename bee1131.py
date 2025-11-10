inter = 0
gremio = 0
empate = 0
grenais = 1
cont = 1
while cont != 0:
    col, gg = input().split()
    col = int(col)
    gg = int(gg)
    if gg > col:
        gremio += 1
    if col > gg:
        inter += 1
    if col == gg:
        empate +=1
    new = int(input('Novo grenal (1-sim 2-nao)\n'))
    if new == 2:
        break
    if new == 1:
        grenais += 1
print(f'{grenais} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empate}')
if gremio > inter:
    print('Gremio venceu mais')
if inter > gremio:
    print('Inter venceu mais')
if empate > inter and empate > gremio:
    print('Nao houve vencedor')       
    