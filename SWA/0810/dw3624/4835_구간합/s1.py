import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    n, m = map(int,input().split())
    numbers = list(map(int, input().split()))
    cnts = [0] * (n - m + 1)

    for i in range(n - m + 1):
        temp = 0
        for j in range(m):
            temp += numbers[i + j]
        cnts[i] = temp

    max_num = min_num = cnts[0]
    for cnt in cnts:
        if cnt < min_num:
            min_num = cnt
        elif cnt > max_num:
            max_num = cnt

    result = max_num - min_num

    print('#{} {}'.format(t, result))