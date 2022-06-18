import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    n, k = map(int, input().split())
    a = list(range(1, 13))
    cnt = 0

    # 가능한 모든 부분집합 탐색
    for i in range(1<<len(a)):
        tmp = []
        for j in range(len(a)):
            if i & (1<<j):
                tmp.append(a[j])

        # 요소의 개수가 n인 부분집합 탐색
        if len(tmp) == n:
            # 요소들의 합 계산
            tmp_sum = 0
            for tmp_t in tmp:
                tmp_sum += tmp_t
            # 합이 k인 경우 cnt 1 증가
            if tmp_sum == k:
                cnt += 1

    print('#{} {}'.format(t, cnt))