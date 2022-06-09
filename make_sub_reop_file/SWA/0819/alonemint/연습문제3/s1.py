from pprint import pprint

import sys
sys.stdin = open('input.txt')

V, E = list(map(int, input().split()))

graph_list = list(map(int, input().split()))

adj = [[0] * (V+1) for _ in range(V + 1)]

for i in range(E):
    n1, n2 = graph_list[2*i: 2*i+2]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

visited = [0] * (V + 1)
name = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
stack = []

# def dfs(v):
#
#     global adj, visited, V
#
#     stack = [v]
#
#     while len(stack):
#         v = stack.pop()
#
#         if visited[v] == 0:
#             visited[v] = 1
#             print(v, visited)
#
#         for w in range(1, V+1):
#             if adj[v][w] == 1 and visited[w] == 0:
#                 stack.append(w)


def dfs(v):
    global adj, visited, V

    stack = [v]

    while stack:
        v = stack.pop()

        if visited[v] == 0:

            visited[v] = 1

        for w in range(1, V+1):
            if visited[w] == 0 and adj[v][w] == 1:
                stack.append(w)
        print(v, visited, stack)


dfs(1)