import sys
sys.stdin = open("input.txt")


def get_search_count(page, target):
    """이진 탐색으로 주어진 페이지를 찾는 탐색 횟수를 구한다.

    page: 책의 총 페이지 수
    target: 찾아야 하는 페이지 번호

    l, r, c: 책의 첫 페이지 / 끝 페이지 / 중간 페이지
    count: 탐색 횟수
    """
    l, r = 1, page
    count = 0

    while True:
        count += 1
        c = (l + r) // 2

        if c == target:
            return count

        if c > target:
            r = c
        else:
            l = c


T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    a_count = get_search_count(P, Pa)
    b_count = get_search_count(P, Pb)
    # result: 이긴 사람 (비긴 경우 0)
    result = 0

    if a_count < b_count:
        result = 'A'
    if a_count > b_count:
        result = 'B'

    print("#{} {}".format(tc, result))
