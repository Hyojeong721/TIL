import sys

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
value = sys.maxsize


def dfs(s, now, visited, depth, temp):
    global value

    if temp > value:
        return

    if depth == N:
        if arr[now][s] != 0:
            temp += arr[now][s]
            value = min(temp, value)
        return

    for idx, val in enumerate(arr[now]):
        if idx not in visited and val != 0 and idx != s:
            visited.append(idx)
            dfs(s, idx, visited, depth+1, temp+val)
            visited.pop()


for i in range(N):
    dfs(i, i, [i], 1, 0)

print(value)
