import sys
sys.stdin = open("input.txt")

# V => 노드, 정점 vertex
# E => 엣지, 간선 edge

V, E = list(map(int, input().split()))
graph_list = list(map(int, input().split()))
print(graph_list)

# 인접행렬
graph = [[0 for _ in range(V+1)]for _ in range(V+1)]   # V+1 * V+1 표 : 0을 더 붙이는 이유는 벽을 만들고, 1부터 시작하기 위함이다.
visited = [0 for _ in range(V+1)]   # 방문지 체크용 리스트 [F F F F F F F F]

for i in range(E):
    startV = graph_list[i*2]
    endV = graph_list[i*2+1]

    # 2개씩 묶어서 연결된 것을 돌린다.
    # 간선의 갯수가 8개라는 것은 8쌍이 들어온다는 것이다.

    # 1 2
    # 1 3
    # 2 4
    # 2 5
    # 4 6
    # 5 6
    # 6 7
    # 3 7

    # 1 1 3
    # 2 2 4
    # 3 3 7
    # ...

    graph[startV][endV] = 1
    graph[endV][startV] = 1     # 무향그래프이므로 좌우 대칭으로 만들어주어야 한다.

def dfs(v):      # 어디서 출발할지? 2라면 2를 기준으로 dfs 진행한다.
    global graph, visited, V

    stack = [v]     # stack에 시작점을 넣고 만들어 시작한다.

    while len(stack):   # stack 이 비어있지 않다면 계속해서 dfs 진행한다.
        v = stack.pop() # stack 이 가진 가장 마지막 요소를 뺀다. 첫 위치를 pop 해서 빼면서, 방문처리 해준다. 마지막 위치가 방문한 곳이면, pop으로 빼준다.
        if visited[v] == 0:   # 마지막 위치가 방문하지 않은 곳이라면
            visited[v] = 1    # 방문을 한다
            print(f'방문한 위치 {v} visited {visited}')

            # 시작점을 기준으로 한 줄 반복 (0번 노드는 없으니 1부터 시작)
            for w in range(1, V+1): # v가 4이면 graph 의 5번째 행(index 4) 리스트를 돈다. <class 'list'>: [0, 0, 1, 0, 0, 0, 1, 0]
                # 간선이 있다 and 방문하지 않았다
                if graph[v][w] == 1 and visited[w] == 0:
                   stack.append(w)


dfs(1) # dfs를 1번 노드를 기준으로 탐색해

