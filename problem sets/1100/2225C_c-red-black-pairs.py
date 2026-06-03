

t=int(input())
for _ in range(t):
    n=int(input())
    r1=list(input())
    r2=list(input())
    pairs=0
    chk=[]

    i=0
    while i<n:
        if r1[i]==r2[i]:
            pairs+=1
        else:
            chk.append(i)
        i+=1

    j=0
    while j<len(chk)-1:
        if chk[j+1]-chk[j]==1:
            if r1[chk[j]]==r1[chk[j+1]]:
                pairs+=1
                j+=2
        j+=1

    k=0
    while k<len(chk)-1:
        if chk[k+1]-chk[k]==1:
            if r1[chk[k]]==r1[chk[k+1]]:
                pairs+=1
                k+=2
        k+=1

    print(n-pairs)