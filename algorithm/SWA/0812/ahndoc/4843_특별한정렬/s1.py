import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 선택 정렬을 이용
    for i in range(N-1):
        max_idx = i
        min_idx = i
        for j in range(i+1, N):
            if numbers[max_idx] < numbers[j]:
                max_idx = j
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        if i % 2 == 0:
            numbers[max_idx], numbers[i] = numbers[i], numbers[max_idx]
        else:
            numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]

    print('#{}'.format(tc), end = ' ')
    for num in numbers[:10]:
        print(num, end = ' ')
    print()

    # for i in range(len(numbers) - 1):
    #     min = i
    #     for j in range(i+1, len(numbers)):
    #         if numbers[min] > numbers[j]:
    #             min = j
    #     numbers[i], numbers[min] = numbers[min], numbers[i]
    #
    # result = []
    # for i in range(1, 6):
    #     result.append(numbers[i * (-1)])
    #     result.append(numbers[i-1])
    #
    # print('#{}'.format(test_case), *result)