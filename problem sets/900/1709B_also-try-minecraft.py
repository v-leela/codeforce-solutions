"""
tags: data structures, dp, implementation
"""

def falldam(list,index,dir):
    if dir==1:
        if list[index]>list[index+1]:
            return list[index]-list[index+1]
        else:
            return 0
    else:
        if list[index]>list[index-1]:
            return list[index]-list[index-1]
        else:
            return 0
        
n,m=map(int,input().split())
a=list(map(int,input().split()))
for _ in range(m):
    s,t=map(int,input().split())
    falldamage=0
    if s<t:
        while s<t:
            falldamage+=falldam(a,s-1,1)
            s+=1
    else:
        while s>t:
            falldamage+=falldam(a,s-1,-1)
            s-=1
    print(falldamage)