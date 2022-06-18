import sys
sys.stdin = open('input.txt')

def is_road(s, g):
    global graph
    visited = [0 for _ in range(100)]
    stack = [s]
    while stack:
        current = stack.pop()
        if visited[current] == 0:
            visited[current] = 1
            for i in range(0, 100):
                if graph[current][i] == 1 and visited[i] == 0:
                    stack.append(i)

    if visited[g] == 1:
        return 1

    else:
        return 0

T = 10

for tc in range(1, T+1):
    tc, edges = map(int, input().split())
    graph = [[0] * (100) for _ in range(100)]

    numbers = list(map(int, input().split()))
    for idx, value in enumerate(numbers):
        if idx % 2:
            graph[numbers[idx - 1]][value] = 1

    print('#{} {}'.format(tc, is_road(0, 99)))