import sys
sys.stdin =open('input.txt')


def dfs(i,idx_list,result):
    global ans
    if i==N:
        ans = min(ans,result)


    for j in range(N):

        if idx_list[j]==0 and result<ans:
            print(i, j)
            print(idx_list)
            idx_list[j]=1
            result += list_n[i][j]
            dfs(i+1,idx_list,result)
            idx_list[j]=0
            result -= list_n[i][j]

for tc in range(1,int(input())+1):

    N = int(input())
    list_n = []
    result = 0
    for _ in range(N):
        list_n.append(list(map(int,input().split())))
    min_list=[]
    idx_list=[0]*N
    result =0
    ans=100000000
    dfs(0,idx_list,result)

    print("#{} {}".format(tc,ans))