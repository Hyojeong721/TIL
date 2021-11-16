import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()

    cnt = 0
    start = 0
    while B in A[start:]:
        cnt += 1
        start += A[start:].index(B) + len(B)

    num = len(A) - cnt * (len(B) - 1)
    print('#{0} {1}'.format(tc, num))