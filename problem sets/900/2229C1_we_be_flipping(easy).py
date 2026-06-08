t=int(input())
for _ in range(t):
    n = int(input()) + 1
    a = list(map(int,input().split()))
    list_a = a + [0]
    index_a = []
    flip = 0
    for i in range(1,n+1):
        if flip:
            list_a[-i] *= -1
        if i == 1:
            continue
        elif list_a[-i] < 0:
            continue
        else:
            index = n-i+1
            index_a.append(index)
            if flip:
                flip = 0
            else:
                flip = 1
 #           for j in range(index):
#                list_a[j] *= -1
#            ele_list = list_a[-i+1:]
#            list_a = nump + ele_list
    print(len(index_a))
    print(" ".join(map(str,index_a)))
