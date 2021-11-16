import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    A, B = input().split( )

    n = len(A)
    m = len(B)
    cnt = 0
    i = 0

    while i < n-m+1:
        if A[i:i+m] == B:
            cnt += 1
            i += m
        else:
            i += 1
    result = n + cnt - (cnt*m)

    print('#{} {}'.format(tc, result))