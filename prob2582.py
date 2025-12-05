n = int(input())
lista = ['PROXYCITY','P.Y.N.G','DNSUEY','SERVERS','HOST!','CRIPTONIZE','OFFILINE DAY','SALT','ANSWER','RAR?','WIFI ANTENNAS']
for k in range (n):
    n1,n2 = map(int,input().split())
    soma = n1+n2
    print(lista[soma])
    