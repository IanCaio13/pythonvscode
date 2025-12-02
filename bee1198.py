while True:
    try:
        n1,n2 = map(int,input().split())
        more = max(n1,n2)
        small = min(n1,n2)
        print(more - small)
    except EOFError:
        break
