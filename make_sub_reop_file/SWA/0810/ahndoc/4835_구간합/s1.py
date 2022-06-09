import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    # sum_list = []
    # result = []
    # for i in range(N - M + 1):
    #     numbers_data = []
    #
    #     for j in range(M):
    #         numbers_data.append(numbers[i + j])
    #
    #     sum_value = sum(numbers_data)
    #     sum_list.append(sum_value)
    #
    # max_value = sum_list[0]
    # for i in range(len(sum_list)):
    #     if max_value < sum_list[i]:
    #         max_value = sum_list[i]
    #
    # min_value = sum_list[0]
    # for i in range(len(sum_list)):
    #     if min_value > sum_list[i]:
    #         min_value = sum_list[i]
    #
    # result = max_value - min_value
    #
    # print('#{} {}'.format(test_case, result))

    # max_v = 0
    # min_v = 500000000
    # for i in range(N-M+1):
    #     temp_max = 0
    #     temp_min = 0
    #     for j in range(M):
    #         temp_max += numbers[i+j]
    #         temp_min += numbers[i+j]
    #     if temp_max > max_v:
    #         max_v = temp_max
    #     if temp_min < min_v:
    #         min_v = temp_min
    # print('#{} {}'.format(tc, max_v - min_v))

    max_v = 0
    min_v = 0
    for i in range(M):
        max_v += numbers[i]
        min_v += numbers[i]

    for i in range(N - M + 1):
        temp = 0
        for j in range(M):
            temp += numbers[i + j]
        if temp > max_v:
            max_v = temp
        if temp < min_v:
            min_v = temp
    print('#{} {}'.format(tc, max_v - min_v))