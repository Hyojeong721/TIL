import sys
sys.stdin = open('input.txt')

# V => 노드, 정점
# E => 엣지, 간선
V, E = list(map(int, input().split()))

# E 쌍의 개수 들어옴 -> 2 * E 개
graph_list = list(map(int, input().split()))

graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]

for i in range(E):
    start = graph_list[2*i]
    end = graph_list[2*i + 1]

    graph[start][end] = 1
    graph[end][start] = 1

def dfs(v):
    global graph, visited, V

    # stack에 시작점을 넣고 시작
    stack = [v]

    # stack이 비어있지 않다면 계속해서 DFS 진행
    while len(stack):
        # 가장 최근에 넣었던 위치를 빼온다
        v = stack.pop()

        # 마지막 위치가 방문하지 않은 곳이라면
        if visited[v] == 0:
            # 방문한다
            visited[v] = 1
            print('방문한 위치 {0} visited {1}'.format(v, visited))

            # 시작점을 기준으로 한 줄 반복 (0번 노드는 없으니 1부터 시작)
            for w in range(1, V + 1):
                # 간선이 있고, 방문하지 않았다면
                if graph[v][w] == 1 and visited[w] == 0:
                    # 스택에 추가
                    stack.append(w)

# dfs를 1번 노드를 기준으로 탐색
dfs(1)