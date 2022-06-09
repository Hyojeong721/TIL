import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = len(arr)

    count = 0
    for i in range(1, 1 << N):
        sum_v = 0
        for j in range(N):
            if i & (1 << j):
                sum_v += arr[j]
        if sum_v == 0:
            count += 1
    if count > 0:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))