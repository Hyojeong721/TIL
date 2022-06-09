import sys
sys.stdin = open('input.txt')


def find_route():
    """
    0에서 99까지 경로 존재하면 1, 아니면 0을 반환.
    :return: boolean
    """
    global graph, visited
    v = 0
    dest = 99
    stack = [0]
    visited[0] = 1

    while True:
        # v 에서 갈 수 있는 길이 존재하고, 그 중 첫 번째 길을 아직 방문 안 했다면
        if graph[0][v] != 0 and visited[graph[0][v]] == 0:
            # 방문하고, 목적지인지 검사
            w = graph[0][v]
            visited[w] = 1
            stack.append(w)
            v = w
            if w == dest:
                return 1

        # 첫 번째 길을 방문했지만, 두 번째 길은 아직 방문 안했다면
        elif graph[1][v] != 0 and visited[graph[1][v]] == 0:
            # 방문하고, 목적지인지 검사
            w = graph[1][v]
            visited[w] = 1
            stack.append(w)
            v = w
            if w == dest:
                return 1

        # 모든 길 방문했으면, 이전 길로 한 칸 되돌아 간다.
        else:
            stack.pop()
            if len(stack):
                v = stack[-1]
            else:
                return 0


for _ in range(10):
    T, E = list(map(int, input().split()))
    edge_list = list(map(int, input().split()))

    graph = [[0 for _ in range(100)] for _ in range(2)]
    visited = [0 for _ in range(100)]

    # directed graph complete
    for i in range(E):
        start = edge_list[2*i]
        end = edge_list[2*i + 1]

        if graph[0][start] == 0:
            graph[0][start] = end
        else:
            graph[1][start] = end

    # find route
    result = find_route()
    print('#{0} {1}'.format(T, result))

'''
graph를 배열 2개로 큰 틀을 정해놔도 되지만, 인접리스트로 해도 되겠구나 ~ (배열은 1개만 만들고 append)
'''