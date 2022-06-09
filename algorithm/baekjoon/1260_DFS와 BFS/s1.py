import sys
sys.stdin = open("input.txt")

def dfs(graph, v):
    dfs_res = []
    s = [v]
    while s:
        temp = s.pop()
        if temp in dfs_res:
            continue
        else:
            dfs_res.append(temp)

        if temp in graph:
            graph[temp].sort(reverse=True)
            for t in graph[temp]:
                s.append(t)
    return dfs_res

def bfs(graph, v):
    bfs_res = []
    q = [v]
    while q:
        temp = q.pop(0)
        if temp in bfs_res:
            continue
        else:
            bfs_res.append(temp)
        if temp in graph:
            graph[temp].sort()
            for t in graph[temp]:
                q.append(t)
    return bfs_res
n, m, v = map(int, input().split())
graph = {}
for i in range(m):
    temp = list(map(int, input().split()))
    if temp[0] not in graph:
        graph[temp[0]] = [temp[1]]
    else:
        graph[temp[0]].append(temp[1])

    if temp[1] not in graph:
        graph[temp[1]] = [temp[0]]
    else:
        graph[temp[1]].append(temp[0])


print(*(dfs(graph, v)))
print(*(bfs(graph, v)))
