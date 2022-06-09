import sys
sys.stdin = open("input.txt")

c = int(input())
N = int(input())
arr = [[i] for i in range(c+1)]
visited = [False]*(c+1)

for i in range(N):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
res = 0
temp = [1]
while temp:
    now = temp.pop()
    for i in arr[now]:
        if not visited[i]:
            res += 1
            visited[i] = True
            temp.append(i)
print(res-1)