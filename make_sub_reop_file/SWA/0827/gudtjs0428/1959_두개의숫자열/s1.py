import sys
sys.stdin = open('input.txt')

def max_sum(A, B):
    pass
    if len(A) > len(B):
        A, B = B, A

    result = 0
    total = 0
    for i in range(len(B) - len(A) + 1):
        for j in range(len(A)):
            total += A[j] * B[i+j]
        if total > result:
            result = total
        total = 0
    return result


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print('#{} {}'.format(test_case, max_sum(A, B)))