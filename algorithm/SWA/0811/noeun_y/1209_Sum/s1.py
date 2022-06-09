
for tc in range(1,10+1):
    N=int(input())
    list_n = []
    for i in range(100):
        list_n.append(list(map(int,input().split())))
    max_n=0
    max_m=0
    sum_r=0
    sum_l=0

    for i in range(100):

        sum_r+=list_n[i][100-1-i]
        sum_l+=list_n[i][i]

        if max_n<sum(list_n[i]):
            max_n=sum(list_n[i])
        sum_j = 0
        for j in range(100):
            sum_j+=list_n[j][i]

        if max_m<sum_j:
            max_m = sum_j

    print(f"#{N} {max(max_n,max_m,sum_l,sum_r)}")