while True:
    v,t = map(int,input().split())
    if v >= -100 and v <= 100 and t >= 0 and t <= 200:
        print(v * t*2)