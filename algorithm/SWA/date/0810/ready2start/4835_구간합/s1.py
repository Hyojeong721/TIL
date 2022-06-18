import sys
sys.stdin = open('input.txt')


def get_prefix_sum(numbers):
    """
    배열 numbers의 누적 합 배열 prefix_sum을 구한다.
    (ex. prefix_sum[2] = numbers[0] + numbers[1] + numbers[2])
    """
    prefix_sum = [0] * len(numbers)
    prefix_sum[0] = numbers[0]

    for i in range(1, len(numbers)):
        prefix_sum[i] = prefix_sum[i - 1] + numbers[i]

    return prefix_sum


def get_max_sum(numbers, length):
    """
    배열 numbers에서 길이가 length인 구간 합의 최대값을 구한다.
    prefix_sum: 배열 numbers의 누적 합 배열
    """
    prefix_sum = get_prefix_sum(numbers)

    max_value = prefix_sum[length - 1]

    for i in range(len(prefix_sum) - length):
        if prefix_sum[i + length] - prefix_sum[i] > max_value:
            max_value = prefix_sum[i + length] - prefix_sum[i]

    return max_value


def get_min_sum(numbers, length):
    """
    배열 numbers에서 길이가 length인 구간 합의 최소값을 구한다.
    prefix_sum: 배열 numbers의 누적 합 배열
    """
    prefix_sum = get_prefix_sum(numbers)

    min_value = prefix_sum[length - 1]

    for i in range(len(prefix_sum) - length):
        if prefix_sum[i + length] - prefix_sum[i] < min_value:
            min_value = prefix_sum[i + length] - prefix_sum[i]

    return min_value


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_sum = get_max_sum(numbers, M)
    min_sum = get_min_sum(numbers, M)

    print("#{0} {1}".format(tc, max_sum - min_sum))
