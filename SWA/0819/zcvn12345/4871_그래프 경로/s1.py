import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1
        graph[end][start] = 2

    S, G = map(int, input().split())

    def dfs(v):
        global graph, visited, V

        stack = [v]

        while len(stack):
            v = stack.pop()

            if visited[v] == 0:
                visited[v] = 1

                for w in range(1, V+1):
                    if graph[v][w] == 1 and visited[w] == 0:
                        stack.append(w)
        return visited[G]

    print('#{0} {1}'.format(tc, dfs(S)))