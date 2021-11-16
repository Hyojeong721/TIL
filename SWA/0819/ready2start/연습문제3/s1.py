import sys
sys.stdin = open("input.txt")


V, E = map(int, input().split())

graph_list = [int(x) for x in input().split()]

graph = [[0] * (V + 1) for _ in range(V + 1)]

visited = [False] * (V + 1)

for i in range(E):
    start, end = graph_list[2 * i], graph_list[2 * i + 1]
    graph[start][end] = 1
    graph[end][start] = 1


def dfs(v):
    """
    깊이 우선 탐색을 통해 그래프 전체를 탐색한다.
    Args:
        v: 시작 노드 (이후 현재 노드를 저장)
    """
    global graph, visited, V

    # 스택에 시작점을 넣고 시작
    stack = [v]

    # 스택이 비어있지 않다면 계속 DFS 진행
    while stack:
        # 가장 최근에 넣었던 위치를 빼온다.
        v = stack.pop()

        # 마지막 위치가 방문하지 않은 곳이라면
        if not visited[v]:
            # 방문한다.
            visited[v] = True
            print("방문한 위치 {} visited {}".format(v, visited))

            for w in range(1, V + 1):
                # v와 w가 연결되어 있고 아직 w를 방문하지 않았다면
                if graph[v][w] and not visited[w]:
                    dfs(w)


dfs(1)
