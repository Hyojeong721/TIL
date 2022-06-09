import sys
sys.stdin = open("input.txt")


def get_max_from_today(prices):
    """
    각 날의 매매가를 인자로 받아서,
    각 날에 대하여 그 날부터 시작하여 가장 높은 매매가를 배열에 담아 반환한다.
        ex. 매매가가 [4, 10, 30, 50, 5, 7]인 경우
            => [50, 50, 50, 50, 7, 7]을 반환

    Args:
        prices: 각 날의 매매가
    Returns:
        max_prices: 각 날에 대하여, 그 날 이후의 최고 매매가
    """
    max_prices = [0] * len(prices)
    max_prices[-1] = prices[-1]

    for i in range(len(prices) - 2, -1, -1):
        if prices[i] > max_prices[i + 1]:
            max_prices[i] = prices[i]
        else:
            max_prices[i] = max_prices[i + 1]

    return max_prices


def get_max_profit(prices):
    """
    각 날의 매매가를 인자로 받아, 얻을 수 있는 최대 이익을 구한다.
    하루에 최대 1만큼 구입할 수 있으며, 판매는 얼마든지 가능하다.

    Args:
        prices: 각 날의 매매가
    Returns:
        total: 최대 이익
    """
    # max_prices: 각 날에 대하여, 그 날 이후의 최고 매매가
    max_prices = get_max_from_today(prices)
    total = 0

    for i in range(len(prices)):
        # 각 날에 대하여, 그 날 물건을 사서 얻을 수 있는 최대 이익을 더한다.
        total += (max_prices[i] - prices[i])

    return total


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = [int(x) for x in input().split()]

    max_profit = get_max_profit(prices)
    print("#{} {}".format(tc, max_profit))
