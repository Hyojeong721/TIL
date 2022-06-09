import sys
sys.stdin = open('input.txt')

T = int(input())
A = list(range(1, 13))

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0

    for i in range(1<<len(A)):
        list = []
        sum = 0
        for j in range(len(A)):
            if i & (1<<j):
                list.append(A[j])
                sum += A[j]

        if len(list) == N and sum == K:
            result += 1

    print('#{} {}'.format(tc, result))