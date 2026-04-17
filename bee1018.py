def note():
    value = int(input())
    print(value)
    hundred_value = value // 100
    value = value % 100
    print(f'{hundred_value} nota(s) de R$ 100,00')
    fifty_value = value // 50
    value = value % 50
    print(f'{fifty_value} nota(s) de R$ 50,00')
    twenty_value = value // 20
    value = value % 20
    print(f'{twenty_value} nota(s) de R$ 20,00')
    ten_value = value // 10
    value = value % 10
    print(f'{ten_value} nota(s) de R$ 10,00')
    five_value = value // 5
    value = value % 5
    print(f'{five_value} nota(s) de R$ 5,00')
    two_value = value // 2
    value = value % 2
    print(f'{two_value} nota(s) de R$ 2,00')
    print(f'{value} nota(s) de R$ 1,00')
note()