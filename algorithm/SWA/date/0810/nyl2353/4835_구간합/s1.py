import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    # 누적합
    prefix_sum = [lst[0]]
    for i in range(1, N):
        prefix_sum.append(lst[i] + prefix_sum[i - 1])

    # 부분합 중 max와 min
    max_sum = prefix_sum[M - 1]
    min_sum = prefix_sum[M - 1]
    for i in range(M, N):
        partial_sum = prefix_sum[i] - prefix_sum[i-M]
        if partial_sum > max_sum:
            max_sum = partial_sum
        if partial_sum < min_sum:
            min_sum = partial_sum

    diff = max_sum - min_sum
    print('#{0} {1}'.format(tc, diff))