import sys
sys.stdin = open('input.txt')

T = int(input())
lst = [1, 3]

for tc in range(1, T+1):
    N = int(input()) // 10
    length = len(lst)
    if N > length:
        for i in range(length, N):
            lst.append(lst[i-1] + 2 * lst[i-2])
    print('#{} {}'.format(tc, lst[N - 1]))

