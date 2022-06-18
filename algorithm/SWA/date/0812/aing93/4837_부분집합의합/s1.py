import sys
sys.stdin = open('input.txt')

# # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
A = list(range(1, 13))

T = int(input())
for tc in range(1, T+1):

    # N=부분집합 원소 개수 # K=부분집합의 합
    N, K = list(map(int, input().split()))

    count = 0
    for i in range(1<<12):
        subset = [] # 부분집합 원소 리스트
        sum_subset = 0 # 부분집합의 합
        for j in range(12):
            if i & (1<<j):
                subset.append(A[j])
                sum_subset += A[j]

        # 부분집합의 원소 개수가 N과 같고 부분집합의 합이 K와 같으면 count +1 증가
        if len(subset) == N and sum_subset == K:
            count += 1

    print('#{} {}'.format(tc, count))

