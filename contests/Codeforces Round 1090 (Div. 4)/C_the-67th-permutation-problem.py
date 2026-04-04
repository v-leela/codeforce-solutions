t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    sub_list=[]
    for i in range(n):
        sub_list=[i+1,n*3-i*2,n*3-i*2-1]
        l.append(i+1)
        l.append(n*3-i*2)
        l.append(n*3-i*2-1)
    print(" ".join(list(map(str,l))))
