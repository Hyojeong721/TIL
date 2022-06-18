import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for e in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1


    S, G = map(int, input().split())


    def dfs(start, end):
        global graph, visited, V
        stack = [start]

        while len(stack) > 0:
            v = stack.pop()

            if visited[v] == 0:
                visited[v] = 1
                # print('방문한 위치 {} visited {}'.format(v, visited))

                if v == end:
                    return 1

                for w in range(1, V+1):
                    if graph[v][w] == 1 and visited[w] == 0:
                        stack.append(w)
        return 0

    result = dfs(S,G)
    print('#{} {}'.format(t, result))