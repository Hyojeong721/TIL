import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    T, N = map(int, input().split())
    graph_list = list(map(int, input().split()))
    graph = [[0] * 100 for _ in range(2)]

    for i in range(0, len(graph_list), 2):
        if graph[0][graph_list[i]] == 0:
            graph[0][graph_list[i]] = graph_list[i+1]
        else:
            graph[1][graph_list[i]] = graph_list[i+1]

    stack = [0]
    result = 0

    while len(stack):
        s = stack[-1]
        if graph[0][s] == 99 or graph[1][s] == 99:
            result = 1
            break
        if graph[0][s] != 0:
            stack.append(graph[0][s])
        elif graph[1][s] != 0:
            stack.append(graph[1][s])
        else:
            stack.pop()
            if len(stack) ==0:
                break
            else:
                if graph[0][stack[-1]] != 0:
                    graph[0][stack[-1]] = 0
                else:
                    graph[1][stack[-1]] = 0
    print('#{} {}'.format(T, result))
