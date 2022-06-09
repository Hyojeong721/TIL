import sys
sys.stdin = open('input.txt')


# V: 노드 E: 간선
V, E = list(map(int, input().split()))

graph_list = list(map(int, input().split()))

# 인접 행렬 (가로*세로 V+1*V+1개(노드 개수 +1)) - 0번 인덱스는 사용X (노드 번호와 인덱스 번호를 맞추기 위해 +1함)
graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

# 방문 기록
visited = [0 for _ in range(V+1)]

for i in range(E): # E: 8
    start = graph_list[i*2]
    end = graph_list[i*2+1]

    # 무향그래프 (방향성이 없음) - 1에서 2로 이동 가능하면 2에서 1로도 가능 (대각선 기준 대칭)
    graph[start][end] = 1
    graph[end][start] = 1

# v: 시작점
def dfs(v):
    global graph, visited, V

    # stack에 시작점을 넣고 시작
    stack = [v]

    # stack이 빌 때까지 DFS 반복
    while len(stack):
        # 가장 마지막에 넣었던 위치를 빼옴
        v = stack.pop()

        # 방문 안했다면(0) 방문함(1)
        if visited[v] == 0:
            visited[v] = 1
            print('방문한 위치 {}, visited {}'.format(v, visited))

            # 시작점을 기준으로 한 줄 반복 (0번 노드가 없기 때문에 1부터 시작)
            for w in range(1, V+1):
                # 간선이 있다면 and 방문하지 않았다면 (v와 w가 연결되어 있는데 w를 방문하지 않았다면)
                if graph[v][w] == 1 and visited[w] == 0:
                    # stack에 추가 (시작점 v가 w로 바뀜)
                    stack.append(w)

# dfs를 1번 노드 기준으로 탐색
dfs(1)