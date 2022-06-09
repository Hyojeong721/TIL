import sys
sys.stdin = open('input.txt')


def get_max_rate(rate, count):
    """
    모든 직원이 일을 성공할 최대 확률을 구한다.
    Args:
        rate: 현재까지 계산한 성공 확률
        count: 현재까지 계산한 직원의 수
    """
    global N, visited, success_rates, max_rate

    # 백트래킹: 현재까지 계산한 확률이 max_rate 이하인 경우, 탐색 종료
    if rate <= max_rate:
        return

    # 모든 직원의 확률을 다 계산한 경우, max_rate와 확률을 비교하고 탐색 종료
    if count == N:
        # 위에서 rate <= max_rate인 경우는 걸렀으므로, 바로 대입 가능
        max_rate = rate
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            new_rate = rate * success_rates[count][i] / 100
            get_max_rate(new_rate, count + 1)
            visited[i] = False


T = int(input())

for x in range(1, T + 1):
    N = int(input())
    visited = [False] * N
    success_rates = []

    for _ in range(N):
        success_rates.append([int(x) for x in input().split()])

    # max_rate: 모든 일을 성공할 최대 확률
    max_rate = 0
    get_max_rate(100, 0)

    print("#{} {:6f}".format(x, max_rate))
