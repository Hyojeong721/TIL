import sys
sys.stdin = open("input.txt")


def count_subset(count, total):
    """
    1부터 12까지의 숫자를 원소로 가지는 집합에 대하여
    원소의 개수가 <count>개이며
    원소의 합이 <total>인 부분집합의 개수를 구한다.

    result: 조건을 만족하는 부분집합의 개수
    cnt_count: 현재 탐색 중인 부분집합의 요소의 개수
    cnt_total: 현재 탐색 중인 부분집합의 요소의 합
    """
    n = 12
    result = 0

    for i in range(1 << n):
        cnt_count, cnt_total = 0, 0
        for j in range(n):
            if i & (1 << j):
                cnt_count += 1
                # 숫자는 1부터 시작하지만 인덱스는 0부터 시작하므로
                # (j + 1)을 더한다.
                cnt_total += (j + 1)

        if cnt_count == count and cnt_total == total:
            result += 1

    return result


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    print("#{} {}".format(tc, count_subset(N, K)))
