import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(S, G):
    global graph, visited, V
    stack = [S]

    while len(stack):

        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1

        for c in range(1, V+1):
            if graph[v][c] == 1 and visited[c] == 0:
                if c == G:
                    return 1
                else:
                    stack.append(c)
    return 0

for tc in range(1, T + 1):

    V, E = map(int, input().split())
    graph_list = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]

    for i in range(E):
        start = graph_list[i][0]
        end = graph_list[i][1]
        # 방향성 그래프
        graph[start][end] = 1


    print('#{} {}'.format(tc, dfs(S, G)))