import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    graph_list = [list(map(int, input().split())) for _ in range(E)]
    visited = [0 for _ in range(V + 1)]
    S, G = list(map(int, input().split()))

    for i in range(E):
        start = graph_list[i][0]
        end = graph_list[i][1]

        graph[start][end] += 1
        graph[end][start] += 1

def find_route(S, G):
    global graph, visited, graph_list

    stack = [S]

    while len(stack):
        S = stack.pop()
        if visited[S] == 0:
            visited[S] += 1

            for

    while len(stack):
