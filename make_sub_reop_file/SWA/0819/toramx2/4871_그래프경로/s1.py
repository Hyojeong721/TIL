import sys
sys.stdin = open('input.txt')

def dfs(S, G):
    global graph, visited, V

    stack = [S]

    while len(stack):
        S = stack.pop()

        if visited[S] == 0:
            visited[S] = 1

            for M in range(1, V+1):
                if graph[S][M] == 1 and visited[M] == 0:
                    stack.append(M)

    if visited[G] == 1:
        return 1
    else:
        return 0


T = int(input())

for test_case in range(1, T+1):
    V, E = list(map(int, input().split()))
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = list(map(int, input().split()))
        graph[v1][v2] = 1

    S, G = list(map(int, input().split()))

    result = dfs(S, G)

    print('#{0} {1}'.format(test_case, result))


