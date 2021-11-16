import sys
sys.stdin = open('input.txt')

# v : 출발 노드
def dfs(v):
    global graph, visited, V
    # stack에 시작점을 넣고 시작 (push v)
    stack = [v]

    # 스택이 비어있지 않다면 계속해서 DFS 진행
    while len(stack):
        # 가장 마지막에 넣었던 위치를 빼온다
        v = stack.pop()

        # 마지막 위치가 방문하지 않은 곳이라면
        if visited[v] == 0:
            visited[v] = 1

            # 시작점을 시준으로 한줄 반복 (0번 노드는 없으니 1부터 시작)
            for w in range(1, V + 1):
                # 간선이 있다면 and 방문하지 않았다면
                if graph[v][w] == 1 and visited[w] == 0:
                    stack.append(w)

T = int(input())

for TC in range(1, T+1):
    answer = 0
    V, E = list(map(int, input().split()))

    graph = [[0] * (V+1) for _ in range(V+1)]
    visited = [0 for _ in range(V + 1)]

    for i in range(E):
        start, end = list(map(int, input().split()))
        graph[start][end] = 1

    # S : 출발 노드
    # G : 도착 노드
    S, G = list(map(int, input().split()))
    dfs(S)
    if visited[G] == 1:
        answer = 1

    print('#{} {}'.format(TC, answer))

