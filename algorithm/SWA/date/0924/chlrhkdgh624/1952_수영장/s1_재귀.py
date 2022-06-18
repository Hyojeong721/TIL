import sys
sys.stdin = open('input.txt')


def calc(cost, m):
    global min_cost
    if m >12:
        if min_cost > cost:
            min_cost = cost
        return
    # 1일권
    calc(cost + d * plan[m], m+1)
    # 1달권
    calc(cost + m1, m+1)
    # 3달권
    calc(cost + m3, m+3)


T = int(input())
for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    min_cost = y  # 1년 이용권을 최저 가격으로 처음에 설정
    calc(0, 1)
    print('#{} {}'.format(tc, min_cost))
