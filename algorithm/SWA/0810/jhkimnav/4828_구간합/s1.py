import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    array = list(map(int, input().split()))
    max = 0
    min = 10000
    for k in range(M):
        max += array[k]
    min = max
    for i in range(0, N-M+1):
        temp = 0
        for j in range(0, M):
            temp += array[i+j]
        if max < temp:
            max = temp
        if min > temp:
            min = temp
    print('#{} {}'.format((test_case), max-min))