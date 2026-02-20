t=int(input())
for i in range(t):
    n = int(input())
    s = input()
    a = []
    for j in range(n):
        b=s
        sep_list=list(b)
        val=int(sep_list[j])
        val=1-val
        sep_list[j]=str(val)
        changed="".join(sep_list)
        a.append(changed)
    all="".join(a)
    count=all.count("1")
    print(count)