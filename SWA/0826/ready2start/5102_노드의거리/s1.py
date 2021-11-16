import sys
sys.stdin = open("input.txt")


def get_distance(adj_list, V, start, end):
    """
    인접 리스트로 주어진 그래프의 출발 노드에서 도착 노드까지의 거리를 구한다.
    (BFS 알고리즘을 통해 구현한다.)

    Args:
        adj_list: 인접 리스트 (그래프)
        V: 그래프의 노드의 개수
        start: 출발 노드
        end: 도착 노드
    Returns:
        출발 노드에서 도착 노드까지의 거리
        (단, 출발 노드에서 도착 노드로 가는 경로가 없다면 0)
    """
    queue = [start]
    distances = [0] * (V + 1)

    while queue:
        # 큐의 맨 앞에 있는 노드(=큐에 가장 먼저 넣은 노드)를 꺼낸다.
        cnt = queue.pop(0)
        # 꺼낸 노드와 인접한 노드를 순회하면서
        for node in adj_list[cnt]:
            # 아직 방문하지 않은 노드라면
            if not distances[node]:
                # 출발 노드로부터의 거리를 계산하고
                distances[node] = distances[cnt] + 1
                # 만약 현재 노드가 도착 노드라면
                if node == end:
                    # 출발 노드로부터의 거리를 리턴한다.
                    return distances[node]
                queue.append(node)

    # 출발 노드에서 도착 노드로 가는 경로가 없다면 0을 리턴한다.
    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj_list = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)

    S, G = map(int, input().split())

    distance = get_distance(adj_list, V, S, G)
    print("#{} {}".format(tc, distance))
