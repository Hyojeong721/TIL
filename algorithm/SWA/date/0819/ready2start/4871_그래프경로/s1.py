import sys
sys.stdin = open('input.txt')


def check_route(graph, v, start, end):
    """그래프의 시작 노드로부터 도착 노드로의 경로가 있는지 확인한다.

    Args:
        graph: 경로 그래프 (2차원 배열의 인접 행렬)
        v: 그래프의 노드의 개수
        start: 시작 노드
        end: 도착 노드
    Returns:
        시작 노드로부터 도착 노드로의 경로가 있으면 True, 없으면 False
    """
    stack = [start]
    visited = [False] * (v + 1)

    while stack:
        cnt = stack.pop()
        visited[cnt] = True

        for i in range(1, v + 1):
            # 현재 노드와 연결되어 있고 아직 방문하지 않은 노드라면
            if graph[cnt][i] and not visited[i]:
                # 도착 노드라면 True를 반환한다.
                if i == end:
                    return True
                # 도착 노드가 아니라면 스택에 추가한다.
                stack.append(i)

    # 출발 노드에서 시작하여 탐색을 종료했지만 도착 노드에 방문하지 않았다면 False를 반환한다.
    return False


T = int(input())

for tc in range(1, T + 1):
    # V: 노드의 개수 / E: 간선의 개수
    V, E = map(int, input().split())
    # graph: 그래프의 경로를 나타내는 인접 행렬
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1

    S, G = map(int, input().split())

    result = int(check_route(graph, V, S, G))
    print("#{} {}".format(tc, result))
