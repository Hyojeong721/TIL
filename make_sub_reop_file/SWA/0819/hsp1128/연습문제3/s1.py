import sys
sys.stdin = open('input.txt')

V, E = list(map(int, input().split()))


graph_list = list(map(int, input().split()))
graph = [[0 for  _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
for i in range(E):
    start = graph_list[i*2]
    end = graph_list[i*2+1]

    graph[start][end] += 1
    graph[end][start] += 1


def dfs(v):
    global graph, visited, V

    stack = [v]

    while len(stack):
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            print(f'방문한 위치 {v} visited {visited}')

            for w in range(1, V+1):
                if graph[v][w] == 1 and visited[w] == 0:
                    stack.append(w)



print(dfs(1))