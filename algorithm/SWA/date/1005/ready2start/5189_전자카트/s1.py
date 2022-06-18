import sys
sys.stdin = open('input.txt')


def get_min_value(cnt, total):
    """
    DFS로 전체 경로를 순회하며 최소 소비량을 구한다.
    Args:
        cnt: 현재 구역 번호
        total: 현재까지의 소비량
    """
    global board, N, visited, min_value

    # 백트래킹 => 현재까지의 소비량이 min_value보다 크거나 같다면, 탐색을 종료한다.
    if total >= min_value:
        return

    # 모든 곳을 방문한 경우 => 최종 소비량을 구한 뒤, min_value와 비교한다.
    if visited == [True] * N:
        min_value = min(min_value, total + board[cnt][0])
        return

    for i in range(1, N):
        if not visited[i]:
            visited[i] = True
            get_min_value(i, total + board[cnt][i])
            visited[i] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = []

    for _ in range(N):
        board.append([int(x) for x in input().split()])

    min_value = 10000
    visited = [False] * N
    visited[0] = True

    get_min_value(0, 0)
    print("#{} {}".format(tc, min_value))
