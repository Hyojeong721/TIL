import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    t, N = map(int, input().split())
    graph = [[0]*101 for _ in range(101)]
    nodes = list(map(int, input().split()))
    visited = [0] * 101
    for node in range(0, len(nodes), 2):
        i = nodes[node]
        j = nodes[node+1]
        graph[i+1][j+1] = 1

    v = 1
    stack = [v]

    while len(stack):
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1

            for w in range(1, 101):
                if graph[v][w] == 1 and visited[w] == 0:
                    stack.append(w)
    print('#{0} {1}'.format(t, visited[100]))