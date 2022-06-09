import sys
sys.stdin = open('input.txt')

# v => 노드 or 정점
# E => 엣지 or 간선
V, E = list(map(int, input().split()))

graph_list = list(map(int, input().split()))
graph = [[0 for _ in range(V+1)] for _ in range(V+1)] # 인덱스를 그대로 숫자로 쓰기 위해 0을 한 줄씩 더 붙임!
visited = [0 for _ in range(V+1)]

# 그래프 그려주기 위해서 한 쌍씩!
for i in range(E): # E == 8
    start = graph_list[i*2]
    end = graph_list[i*2+1]
    graph[start][end] = 1
    graph[end][start] = 1 # 얘는 방향이 없으므로

def dfs(v):
    global graph, visited, V
    stack = [v] # 시작 지점을 스택에 넣어줌

    # 스택이 비어있지 않다면 계속해서 DFS 진행
    while len(stack):
        # 가장 마지막에 넣었던 위치를 빼온다
        v = stack.pop()
        # 마지막 위치가 방문하지 않은 곳이라면
        if visited[v] == 0:
            visited[v] = 1
            print('방문한 위치 {} visited {}'.format(v, visited))


            # 시작점을 기준으로 한 줄 반복(0번 노드는 없으니 1번부터 시작)
            for w in range(1, V+1):
                # 간선이 있다면 and 방문하지 않았다면
                if graph[v][w] == 1 and visited[w] == 0:
                    # 스택에 추가
                    stack.append(w)

# dfs를 탐색해줘
dfs(1)