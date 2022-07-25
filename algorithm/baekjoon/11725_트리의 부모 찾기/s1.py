import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)

N = int(input())
arr = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
visited[1] = 1

for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)

def dfs(s):
    for x in arr[s]:
        if visited[x] == 0:
            visited[x] = s
            # print("dfs(",s,")")
            dfs(x)

dfs(1)

# print("=======")
for k in range(2, N+1):
    print(visited[k])
