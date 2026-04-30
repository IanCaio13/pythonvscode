def contar():
    entradas = 0
    saídas = 0
    movi = 0
    while True:
        type_ = input('Digite o tipo (E/S ou 0 para sair)')
        if type_ == 'E' or type_ == 'e':
            valueagree = float(input())
            entradas += valueagree
            movi += 1
        elif type_ == 'S' or type_ == 's':
            valuedesagree = float(input())
            saídas += valuedesagree
            movi += 1
        elif type_ == '0':
            print (f'---RELATÓRIO---\nEntradas: R${entradas:.2f}\nSaídas: R${saídas:.2f}\nSaldo Final: R${entradas - saídas:.2f}\nMovimentações: {movi}')
            break
        else:
            print('(comando inválido)')
contar()
        



