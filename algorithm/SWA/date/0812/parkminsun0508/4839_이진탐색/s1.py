# 4839 이진탐색
# 이진탐색 게임에서 이긴 사람 알아내기

import sys
sys.stdin = open("input.txt")

# 이진 탐색 결과에 대한 함수를 만들어준다.
def bin_search(p, key):
    l = 1
    cnt = 0
    while True:
        cnt += 1
        center = (l + p) // 2
        if key < center:
            p = center
        elif center < key:
            l = center
        else:
            return cnt

# 테스트 케이스 불러오기
T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    page_A = bin_search(P, A)
    page_B = bin_search(P, B)

    if page_A > page_B:
        winner = 'B'
    elif page_A < page_B:
        winner = 'A'
    else:
        winner = 0

    print('#{} {}'.format(tc, winner))

