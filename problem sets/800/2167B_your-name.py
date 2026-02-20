'''
tags: sortings, strings
'''

t=int(input())
for i in range(t):
    length=int(input())
    name=input()
    names_list=name.split()
    name_1=names_list[0]
    name_2=names_list[1]
    name_1_list=list(name_1)
    name_2_list=list(name_2)
    for i in name_1_list:
        if i in name_2:
            index=name_2.find(i)
            name_2_list.pop(index)
            name_2="".join(name_2_list)
    if len(name_2_list):
        print("NO")
    else:
        print("YES")
