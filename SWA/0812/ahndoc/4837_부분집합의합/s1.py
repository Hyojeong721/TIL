import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    A = list(range(1, 13))
    count = 0

    for i in range(1<<12):
        arr = []
        sum_arr = 0
        for j in range(12):
            if i & (1<<j):
                arr.append(A[j])
                sum_arr += A[j]
        if len(arr) == N and sum_arr == K:
            count += 1
    print('#{} {}'.format(test_case, count))


