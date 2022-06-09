import sys
sys.stdin = open('input.txt')

# V => 노드, 정점
# E => 엣지, 간선
V, E = map(int, input().split())
graph_list = list(map(int, input().split()))
graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
for i in range(E):
    start =  graph_list[i*2]
    end = graph_list[i*2+1]

    graph[start][end] = 1
    graph[end][start] = 1
    # graph[graph_list[2*i]][graph_list[2*i+1]] = 1

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        t = q.pop(0)

        for i in range(1, V+1):
            if graph[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1
                print('{}을 방문'.format(i))

# bfs(1)

def bfs2(v):
    queue = [v]

    while queue:
        v = queue.pop(0)

        if not visited[v]:
            visited[v] = 1
            print('{}를 방문'.format(v))
            for w in range(1, V+1):
                if graph[v][w] and visited[w] == 0:
                    queue.append(w)

bfs2(1)





