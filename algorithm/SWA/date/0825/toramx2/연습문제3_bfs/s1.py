import sys
sys.stdin = open('input.txt')

# V - 노드, E - 엣지
V, E = list(map(int, input().split()))
graph_list = list(map(int, input().split()))

graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(E):
    start = graph_list[i*2]
    end = graph_list[i*2+1]

    graph[start][end] = 1
    graph[end][start] = 1

def bfs(v):
    queue = [v]

    while len(queue):
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1

            for w in range(1, V+1):
                if graph[v][w] and visited[w] == 0:
                    queue.append(w)





bfs(1)