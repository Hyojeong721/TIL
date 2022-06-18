import sys
sys.stdin = open('input.txt')


# V = 노트, 정점
# E = 엣지, 간선
V, E = list(map(int, input().split()))

graph_list = list(map(int, input().split()))

# 인접 행렬
graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

visited = [0 for _ in range(V+1)]

for i in range(E):
    start = graph_list[i*2]
    end = graph_list[i*2+1]

    graph[start][end] = 1
    # 무향 그래프이므로 대칭되도록
    graph[end][start] = 1

def dfs(v):
    # 큐에 현재 위치 넣고 시작
    queue = [v]

    # 큐가 빌 때까지
    while len(queue):
        # 큐의 첫번째 위치(출발점)부터 pop해서 시작
        v = queue.pop(0)
        # 방문하지 않았다면
        if not visited[v]:
            # 방문 체크
            visited[v] = 1
            # v=현재 위치, visited=방문한 전체 리스트
            print('{}을 방문했습니다. {}'.format(v, visited))

            # w=가야할 곳
            for w in range(1, V+1):
                # v(현재위치)와 w(가야할 곳)dl 연결되어 있고 w를 방문하지 않았으면
                if graph[v][w] and visited[w] == 0:
                    # 큐에 w를 추가함(갈 예정)
                    queue.append(w)

# 1번 노드 기준
dfs(1)