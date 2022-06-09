import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    N = a[0]
    M = a[1]
    num = list(map(int, input().split()))
    sum_num = 0
    for i in range(0, M):
        sum_num += num[i]

    max_num = sum_num
    min_num = sum_num

    for i in range(M, len(num)):
        sum_num -= num[i-M]
        sum_num += num[i]
        if sum_num > max_num:
            max_num = sum_num
        if sum_num < min_num:
            min_num = sum_num
    print(f'#{test_case} {max_num - min_num}')