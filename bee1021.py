def notas_e_moedas():
    number = float(input())
    note_hundred = number // 100
    
    number = number % 100
    note_fifty = number // 50
    number = number % 50
    note_twenty = number // 20
    number = number % 20
    note_ten = number // 10
    number = number % 10
    note_five = number // 5
    number = number % 5
    note_two = number // 2
    number = number % 2
    print('NOTAS:')
    print(f'{note_hundred:.0f} nota(s) de R$ 100.00')
    print(f'{note_fifty:.0f} nota(s) de R$ 50.00')
    print(f'{note_twenty:.0f} nota(s) de R$ 20.00')
    print(f'{note_ten:.0f} nota(s) de R$ 10.00')
    print(f'{note_five:.0f} nota(s) de R$ 5.00')
    print(f'{note_two:.0f} nota(s) de R$ 2.00')

    hundred_coin = number // 1
    number = number % 1
    fifty_coin = number // 0.5
    number = number % 0.5
    twenty_five_coin = number // 0.25
    number = number % 0.25
    ten_coin = number // 0.10
    number = number % 0.10
    five_coin = number // 0.05
    number = number % 0.05
    one_coin = number / 0.01
    print('MOEDAS:')
    print(f'{hundred_coin:.0f} moeda(s) de R$ 1.00')
    print(f'{fifty_coin:.0f} moeda(s) de R$ 0.50')
    print(f'{twenty_five_coin:.0f} moeda(s) de R$ 0.25')
    print(f'{ten_coin:.0f} moeda(s) de R$ 0.10')
    print(f'{five_coin:.0f} moeda(s) de R$ 0.05')
    print(f'{one_coin:.0f} moeda(s) de R$ 0.01')
notas_e_moedas()





