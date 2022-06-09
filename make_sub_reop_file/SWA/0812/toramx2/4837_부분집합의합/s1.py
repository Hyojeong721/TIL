import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    A = list(range(1, 13))
    count = 0

    for i in range(1 << len(A)):
        total = []
        for j in range(len(A)):
            if i & (1 << j):
                total.append(A[j])

        if len(total) == N and sum(total) == K:
            count += 1

    print('#{0} {1}'.format(test_case, count))