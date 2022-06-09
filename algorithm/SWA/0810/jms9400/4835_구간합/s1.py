import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split())) # N : 정수의 개수, M : 구간의 개수
    case = list(map(int, input().split()))
    total = []
    sum_case = 0


    for i in range(0, N-M+1):
        temp = case[i:i+M]
        for j in temp:
            sum_case += j
        total.append(sum_case)
        sum_case = 0

    max_num = total[0]
    min_num = total[0]
    for num in total:
        if num >= max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    print('#{} {}'.format(test_case, max_num-min_num))



