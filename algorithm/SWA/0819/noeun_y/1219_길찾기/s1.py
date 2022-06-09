import sys
sys.stdin = open("input.txt")

def dfs(load_list,S):
    global ans
    visited[S]=1
    if S == 99:
        ans = 1
        return

    for i in load_list[S]:
        if visited[i]==0:
            dfs(load_list,i)

for tc in range(1,10+1):
    case,n_load = map(int,input().split())
    load_list = [[] for _ in range(n_load+1)]
    visited=[0]*100
    ans=0
    input_load = list(map(int,input().split()))
    for i in range(0,len(input_load),2):
        load_list[input_load[i]].append(input_load[i+1])
    #print(load_list)

    dfs(load_list,0)

    print("#{} {}".format(tc,ans))