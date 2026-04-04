t=int(input())
for _ in range(t):
    lista=list(map(int,input().split()))
    mx=max(lista)
    lista.remove(mx)
    print((-1*sum(lista))+mx)
