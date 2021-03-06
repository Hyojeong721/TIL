import sys
sys.stdin = open('input.txt')

# V => 노드, 정점
# E => 엣지, 간선
V, E = map(int, input().split())
graph_list = list(map(int, input().split()))
graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]

for i in range(E):
    start = graph_list[2*i]
    end = graph_list[2*i+1]
    graph[start][end] = 1
    graph[end][start] = 1

def bfs(v):
    queue = [v]

    while len(queue):
        v = queue.pop(0)

        # 방문하지 않았다면
        if not visited[v]:
            visited[v] = 1
            print('{}번을 방문했습니다. {}'.format(v, visited))

            for w in range(1, V + 1):
                if graph[v][w] and not visited[w]:
                    queue.append(w)

bfs(1)