import sys
sys.stdin = open('input.txt')

# def dfs(s, g):
#     global graph, visited, V
#     stack = [s]
#     visited = [0] * (V + 1)
#
#     while stack:
#         v = stack.pop()
#
#         if visited[v] == 0:
#             visited[v] = 1
#
#             for w in range(1, V + 1):
#                 if graph[v][w] == 1 and visited[w] == 0:
#                     stack.append(w)
#     if visited[g]:
#         return 1
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = list(map(int, input().split()))
#     graph_list = [list(map(int, input().split())) for _ in range(E)]
#     S, G = list(map(int, input().split()))
#     graph = [[0] * (V+1) for _ in range(V+1)]
#
#     for i in range(E):
#         graph[graph_list[i][0]][graph_list[i][1]] = 1
#
#     print('#{} {}'.format(tc, dfs(S, G)))


def dfs(s, g):
    global ans
    visited[s] = 1

    if visited[g]:
        ans = 1
        return

    for t in range(1, V+1):

        if graph[s][t] and not visited[t]:
            dfs(t, g)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = list([0] * (V + 1) for _ in range(V + 1))
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1
    S, G = map(int, input().split())

    ans = 0
    visited = [0] * (V + 1)

    dfs(S, G)
    print('#{} {}'.format(tc, ans))