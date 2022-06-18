import sys
sys.stdin = open('input.txt')

def dfs(start, end):
    stack = []
    # visited = [0 for _ in range(V + 1)]
    visited = [0] * (V + 1)
    # 시작점을 스택에 삽입
    stack.append(start)
    # 스택이 빌때까지 반복문
    while stack:
        # 현재 스택을 꺼내어 현재 값에 할당
        now = stack.pop()
        # 방문 표시
        visited[now] = 1
        for next in range(1, V+1):
            # 만약 방문하지 않았고 연결되어 있다면 (값이 1이라면)
            if not visited[next] and graph[now][next]:
                # 갈 수 있는 곳이므로 스택에 더한다
                stack.append(next)
    # 만약 끝점에 들렀다면 리턴에 1 아니라면 0 표시
    if visited[end]:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    # 노드와 간선 받아옴
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    # 간선 E 만큼 반복하면서 연결되어 있는지 파악
    for i in range(E):
        # 시작점과 끝점 받아옴
        start, end = map(int, input().split())
        # 해당하는 인접행렬에 할당. 방향성이 있음
        graph[start][end] = 1
    # 검사를 위한 시작점과 끝점 받아옴
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, dfs(S, G)))