import sys
sys.stdin = open('input.txt')


def get_min_cost(count, cost):
    """
    전체 제품의 최소 생산 비용을 구한다. (전역변수 min_cost에 저장)
    Args:
        count: 현재까지 포함시킨 제품의 개수
        cost: 현재까지 계산한 제품의 생산 비용
    """
    global N, board, visited, min_cost

    # 백트래킹 : 현재까지 계산한 비용이 min_cost 이상이라면 탐색 종료
    if cost >= min_cost:
        return

    # 전체 제품의 생산 비용을 모두 계산한 경우
    if count >= N:
        min_cost = min(min_cost, cost)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            get_min_cost(count + 1, cost + board[count][i])
            visited[i] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = []

    for _ in range(N):
        board.append([int(x) for x in input().split()])

    visited = [False] * N
    min_cost = 10000

    get_min_cost(0, 0)
    print("#{} {}".format(tc, min_cost))
