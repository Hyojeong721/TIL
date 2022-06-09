import sys
sys.stdin = open('input.txt')

V, E = list(map(int, input().split()))
# V: 노드 혹은 정점
# E: 엣지 혹은 간선

connect = list(map(int, input().split()))

graph = [[0]*(V+1) for _ in range(V+1)]

visited = [0]*(V+1)

for i in range(E):
    a = connect.pop(0)
    b = connect.pop(0)
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(s):
    global graph, visited, V
    stack = [s]

    while len(stack):
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1
            print(f'현재위치: {v}, visited status:{visited}')

            for w in range(1, V+1):
                if graph[v][w] == 1 and visited[w] == 0:
                    stack.append(w)



dfs(1)

