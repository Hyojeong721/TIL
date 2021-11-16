import sys
sys.stdin = open("input.txt")


def check_route(c1, c2, start, end):
    """
    주어진 그래프에서 출발점에서 도착점으로 가는 경로가 있는지 확인한다.

    Args:
        c1, c2: 연결 데이터를 저장한 배열
        (ex. c1[i] = k라면, i에서 k로 가는 경로가 존재한다.)
        start: 출발점
        end: 도착점
    Returns:
        출발점에서 도착점으로 가는 경로가 있으면 True, 없으면 False
    """
    stack = [start]
    visited = [False] * 100
    visited[0] = True

    while stack:
        cnt = stack.pop()

        node1, node2 = c1[cnt], c2[cnt]
        # 현재 위치와 연결된 지점 중 도착점이 있다면 True를 리턴한다.
        if end in (node1, node2):
            return True

        if node1 and not visited[node1]:
            stack.append(node1)
            visited[node1] = True

        if node2 and not visited[node2]:
            stack.append(node2)
            visited[node2] = True

    return False


# 테스트 케이스의 개수가 정해지지 않았으므로
while True:
    # 일단 한 줄을 입력받은 다음
    try:
        tc, route_count = map(int, input().split())
    # EOF(End Of File) 오류가 발생하는 경우 순회를 종료한다.
    except EOFError:
        break

    routes = [int(x) for x in input().split()]

    connections1 = [0] * 100
    connections2 = [0] * 100

    for i in range(route_count):
        start, end = routes[2 * i], routes[2 * i + 1]
        # start에서 시작하는 경로 하나가 이미 저장되어 있다면
        if connections1[start]:
            # 새로운 경로는 connections2 배열에 저장한다.
            connections2[start] = end
        # start에서 시작하는 첫 번재 경로라면 connections1 배열에 저장한다.
        else:
            connections1[start] = end

    result = check_route(connections1, connections2, 0, 99)

    print("#{} {}".format(tc, int(result)))
