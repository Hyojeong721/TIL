import sys
sys.stdin = open('input.txt')



# 시작점과 도착점을 입력하면 연결되어 있는지 여부(0, 1)를 반환하는 함수
def dfs(S, G):
    global graph, V

    stack = [S]
    visited = [0 for _ in range(V+1)]

    while len(stack) > 0:
        S = stack.pop()

        if visited[S] == 0:
            visited[S] = 1

            for n in range(1, V+1):
                if graph[S][n] == 1 and visited[n] == 0:
                    stack.append(n)
    return visited[G]


# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, T + 1):
    # V: 노드 수 E: 간선 수
    V, E = list(map(int, input().split()))

    graph_list = [(list(map(int, input().split()))) for _ in range(E)]

    # 간선 반영한 그래프(graph)
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        start = graph_list[i][0]
        end = graph_list[i][1]

        graph[start][end] = 1

    # S: 시작점, G: 도착점
    S, G = map(int, input().split())

    result = dfs(S, G)
    print('#{} {}'.format(tc, result))
