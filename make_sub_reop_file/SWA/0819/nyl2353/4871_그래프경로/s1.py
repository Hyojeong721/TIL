import sys
sys.stdin = open('input.txt')


def find_route(S, G):
    """
    vertex S 에서 vertex G까지 경로가 존재하면 1, 아니면 0을 반환하는 함수
    :param S: start vertex
    :param G: goal vertex
    :return: boolean
    """
    global graph, visited, V
    stack = [S]
    visited[S] = 1
    v = S

    while True:
        # 오름차순으로 모든 vertex 탐색
        for w in range(1, V + 1):
            # v 에서 갈 수 있지만 아직 방문하지 않은 vertex 있으면 방문하고, goal 인지 검사
            if graph[v][w] == 1 and visited[w] == 0:
                visited[w] = 1
                stack.append(w)
                v = w
                if w == G:
                    return 1
                break
            # v 에서 모든 연결된 vertex 를 방문했다면 pop 하고, v를 가장 마지막 방문한 vertex 로 지정
            elif w == V:
                stack.pop()
                if len(stack):
                    v = stack[-1]
                else:
                    return 0


T = int(input())
for tc in range(1, T + 1):
    # vertex, edge
    V, E = list(map(int, input().split()))

    # pairs of directional edge
    graph_list = []
    for _ in range(E):
        graph_list.extend(list(map(int, input().split())))

    # start, goal
    S, G = list(map(int, input().split()))

    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]

    # graph complete
    for i in range(E):
        start = graph_list[2*i]
        end = graph_list[2*i + 1]
        graph[start][end] = 1

    # find route between vertices
    result = find_route(S, G)
    print('#{0} {1}'.format(tc, result))