import sys
sys.stdin = open('input.txt')

T = int(input())
A = list(range(1, 13))
for tc in range(1, T+1):
    # 부분집합 원소의 수= N / 부분집합의 합 = K
    N, K = map(int, (input().split()))
    result = 0
    # 전체 부분집합 구하기
    for i in range(1 << len(A)):
        zip_list = []
        total = 0
        for j in range(len(A)):
            if i & (1<<j):
                zip_list.append(A[j])
                total += A[j]

        if len(zip_list) == N and total == K:
            result += 1

    print('#{} {}'.format(tc, result))