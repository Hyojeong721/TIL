import sys
sys.stdin = open('input.txt')

# V: 노드, 정점
# E: 엣지, 간선

V, E = map(int, input().split())

graph_list = list(map(int, input().split()))

graph = [[0] * (V + 1) for _ in range(V + 1)]

visited = [0] * (V + 1)

for i in range(E): # 여기서는 8
    start = graph_list[i * 2]
    end = graph_list[i * 2 + 1]

    graph[start][end] = 1
    graph[end][start] = 1

def bfs(v):
    queue = [v]
    while len(queue):
        v = queue.pop(0)
        # 방문하지 않았다면
        if not visited[v]:
            visited[v] = 1
            # print('{}을 방문했습니다. {}'.format(v, visited)) 라고 하면 3의 거리를 가진 6이 가장 늦게 나옴.

            for w in range(1, V + 1): # 0번 노드는 없으니까.
                if graph[v][w] and visited[w] == 0:
                    queue.append(w)


bfs(1) # 1번 노드부터 시작해 주세요~




# 결과적으로 우리의 코드에서는 BFS와 DFS의 차이는 큐에 넣느냐 스택에 넣느냐의 차이!
