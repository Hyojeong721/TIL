import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_val = 0
    min_val = 10000 * M

    for j in range(N-M+1):
        temp_val = 0

        for k in range(j, M+j):
            temp_val += numbers[k]

        if max_val < temp_val:
            max_val = temp_val

        if min_val > temp_val:
            min_val = temp_val

    result = max_val - min_val
    print('#{} {}'.format(i+1, result))