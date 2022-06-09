import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    k = A.count(B)
    # result = 0
    #
    # if B in A:
    #     while B in A:
    #         A = A.replace(B, '')
    #     result = len(A) + k
    #     print('#{} {}'.format(tc, result))
    #
    # else:
    #     result = len(A)
    #     print('#{} {}'.format(tc, result))

    cnt = 0
    i = 0
    while i < len(A) - len(B) + 1:
        if A[i:i+len(B)] == B:
            cnt += 1
            i += len(B)
        else:
            i += 1
    result = len(A) - cnt * len(B) + cnt
    print('#{} {}'.format(tc, result))
