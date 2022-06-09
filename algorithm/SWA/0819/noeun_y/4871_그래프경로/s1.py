import sys
sys.stdin = open("input.txt")


def dfs(load,S,G, visited):
    visited[S]=1

    for i in range(V+1):

        if load[S][i]==1 and visited[i]==0:
            dfs(load,i,G,visited)


for tc in range(1,int(input())+1):
    V,E = map(int,input().split())
    load =[ [0]* (V+1) for i in range(V+1)]
    visited=[0]*(V+1)

    for _ in range(E):
        start,end = map(int,input().split())
        load[start][end]= 1
    S,G = map(int,input().split())

    dfs(load,S,G,visited)
    if visited[G]==1:
        print("#{} 1".format(tc))

    else:
        print("#{} 0".format(tc))
