import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    answer = 0
    arr = list(map(int, input().split()))
    n = len(arr)

    for i in range(1 << n):
        sum = 0
        for j in range(n + 1):
            if i & (1 << j):
                # print(arr[j], end=", ")
                sum += arr[j]
                if sum == 0:
                    answer = 1
                    break
    print('#{} {}'.format(test_case, answer))
