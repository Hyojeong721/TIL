import sys
sys.stdin = open('input.txt')


A = 0
B = 99

T = 10
for tc in range(1, T+1):

    case_n, E = input().split()
    graph_list = list(map(int, input().split()))

    graph = [[0]*100 for _ in range(2)]

    for i in range(len(graph_list)//2):
        if graph[0][graph_list[i*2]] == 0:
            graph[0][graph_list[i * 2]] = graph_list[i*2+1]
        if graph[0][graph_list[i*2]] != 0:
            graph[1][graph_list[i * 2]] = graph_list[i * 2 + 1]

    stack = [0]
    while stack:
        v = stack[-1]
        if graph[0][0] == 99 or graph[1][0] == 99:
            result = 1
            break
        if graph[0][0] != 99:
            stack.append(graph[0][0])
            v = stack.pop()

            if [i]