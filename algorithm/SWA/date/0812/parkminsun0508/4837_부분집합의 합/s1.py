# 4837 부분집합의 합

import sys
sys.stdin = open("input.txt")
# 테스트 케이스 개수를 받아온다.
T = int(input())
# 테스트 케이스 별 부분집합 원소의 수 N은 1<= N <= 12 이다.
N = list(range(1, 13))
for tc in range(1, T+1):
    n, k = map(int, input().split())
    # 답이 될 result 초기화 후 시작
    result = 0
    for i in range(1 << len(N)):
        subset = []
        cnt = 0
        for j in range(len(N)):
            if i & (1 << j):
                subset.append(N[j])
                cnt += 1
        if cnt == n and sum(subset) == k:
            result += 1

    print('#{} {}'.format(tc, result))

