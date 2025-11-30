while True:
    victory_to_one = 0
    victory_to_second = 0
    test_cases = int(input())
    if test_cases == 0:
        break
    for k in range(test_cases):
        n,n1 = map(int,input().split())
        if n > n1:
            victory_to_one += 1
        elif n1 > n:
            victory_to_second += 1
    print(victory_to_one, victory_to_second)
