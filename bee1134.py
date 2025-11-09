alcool = 0
gaso = 0 
diesel = 0
cont = 1
while cont != 0:
    digite = int(input())
    if digite == 1:
        alcool += 1
    if digite == 2:
        gaso += 1
    if digite == 3:
        diesel += 1
    if digite == 4:
        break
print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gaso}\nDiesel: {diesel}')      
