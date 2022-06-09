# 순열 조합 부분집합 재귀로 알아둘것(백트래킹 위해서). DFS BFS 도
# 백트래킹 = dfs(재귀) + 가지치기

def perm(n, k):
    if n == k:
        print(p)
    else:
        for i in range(n):
            if u[i] == 0:
                u[i] = 1
                p[k] = arr[i]
                perm(n, k+1)
                u[i] = 0

N = 3
arr = [1, 2, 3]
p = [0] * N
u = [0] * N
perm(N, 0)
