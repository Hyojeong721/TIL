import sys
sys.stdin = open("input.txt")

def dfs(si,sj):
    global result
    for i in range(4): #상하좌우
        if si+di[i] in range(N) and sj+dj[i] in range(N):
            if load[si + di[i]][sj + dj[i]] == 3:
                result = 1
                return
            if load[si + di[i]][sj + dj[i]] == 0:
                load[si + di[i]][sj + dj[i]]=10
                dfs(si + di[i], sj + dj[i])


for tc in range(1,int(input())+1):
    N = int(input())
    load=[]
    for _ in range(N):
        load.append(list(map(int,input())))

    for i in range(N):
        for j in range(N):
            if load[i][j]==2:
             si,sj=i,j
    di = [0,0,-1,1]
    dj = [1,-1,0,0]
    result = 0
    dfs(si,sj)
    print("#{} {}".format(tc,result))