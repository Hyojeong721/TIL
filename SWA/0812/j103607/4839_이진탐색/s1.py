import sys
sys.stdin = open('input.txt')

# 타겟 페이지 찾는 함수 선언
def find_page(total_page, target):

    l = 1
    r = total_page

    count = 0
    while True:
        c = int((l+r)/2)
        count += 1

        if c == target:
            return count

        elif c < target:
            l = c

        else:
            r = c


# 테스트 케이스
T = int(input())
for tc in range(1, T+1):

    # P=전체 쪽 수
    # A=A가 찾을 쪽 번호 B=B가 찾을 쪽 번호
    P, A, B = list(map(int, input().split()))

    A_count = find_page(P, A)
    B_count = find_page(P, B)

    if A_count < B_count:
        result = 'A'
    elif A_count > B_count:
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(tc, result))

