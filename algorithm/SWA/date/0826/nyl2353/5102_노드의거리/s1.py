import sys
sys.stdin = open('input.txt')


def bfs(S, G):
    """
    S와 G사이 길이 존재한다면 간선의 갯수를 반환. 길이 없으면 0을 반환하는 함수

    :param S: 출발지
    :param G: 목적지
    :return: (constant)
    """
    # 초기화
    q = [0] * V
    front = -1
    rear = -1
    visited = [0] * (V + 1)

    # 시작점 인큐, 방문
    rear += 1
    q[rear] = S
    visited[S] = 1

    # 큐가 비어있지 않으면
    while front != rear:
        # dequeue 하고 현재 위치로 설정
        front += 1
        v = q[front]
        for w in range(1, V + 1):
            # 현재 위치에 인접하고 미방문인 모든 w 노드
            if graph[v][w] and not visited[w]:
                rear += 1
                q[rear] = w
                visited[w] = visited[v] + 1
                if w == G:
                    return visited[w] - 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))

    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for edge in edges:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1

    result = bfs(S, G)
    print('#{} {}'.format(tc, result))