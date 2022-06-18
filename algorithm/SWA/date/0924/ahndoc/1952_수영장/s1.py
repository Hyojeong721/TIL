import sys
sys.stdin = open('input.txt')


"""
완전 탐색 기법
모든 경우의 수 계산하기(재귀함수)


N-1월 요금 -> N월 요금 -> N+1월 요금
N-1월 요금을 다음달(N월)로 넘겨줘서 합산
    '''
    N월까지의 요금 = N-1월 요금 + N월 요금
    N+1월까지의 요금 = N월 요금 + N+1월 요금
    '''
    
N월 요금-> 'N-1월 요금 + N월을 1일권으로 계산한 요금', 'N-1월 요금 + N월을 1달권으로 계산한 요금', 'N-3월 요금 + N월을 3달권 사용할 시 요금' 중 최소값
 
단, '1일권 사용할 경우 요금'과 '1달권 사용할 경우 요금'을 묶어서 최소값을 한번에 구하면 가지치기 가능
 
재귀함수 만들 때, 
base case을 포함한 if문 잘 설정하기 (특히 return 위치)

"""


# # cost: 이전 달까지의 계산 결과, m: 현재 내가 보낼 결과
# def calc(cost, m):
#     global min_cost
#     if m > 12:
#         if min_cost > cost:
#             min_cost = cost
#         return
#     # 1일권
#     calc(cost + d*plans[m], m+1)
#     # 1달권
#     calc(cost + m1, m+1)
#
#     # 1일권 + 1달권 가지치기
#     # calc(cost+min(d*month[m], m1), m+1)
#
#     # 3달권
#     calc(cost + m3, m+3)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     d, m1, m3, y = map(int, input().split())
#     plans = [0] + list(map(int, input().split()))
#     # print(plans)
#
#     min_cost = y # 1년치 비용이 현재 최저의 가격
#
#     calc(0, 1)
#     print(min_cost)
#
# #####################################
# DP로 계산
# T = int(input())
# for tc in range(1, T+1):
#     d, m1, m3, y = map(int, input().split())
#     plans = [0] + list(map(int, input().split()))
#     # 해당 월까지 최소 비용을 저장
#     dp = [0] * 13
#
#     dp[1] = min(d*plans[1], m1)
#     dp[2] = dp[1] + min(d*plans[2], m1)
#     for i in range(3, 13):
#         # dp[i] = min(d*plans[i], m1, m3)
#         dp[i] = min(dp[i-1] + d*plans[i], dp[i-1] + m1, dp[i-3] + m3)
#     # print(dp)
#     print(min(dp[12], y))


def calc(cost, m):
    global min_cost

    if m > 12:
        if cost < min_cost:
            min_cost = cost
        return

    # calc(cost+d*month[m], m+1)
    # calc(cost+m1, m+1)
    calc(min(cost+d*month[m], cost+m1), m+1)
    calc(cost+m3, m+3)


T = int(input())
for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    # print(month)
    min_cost = y
    for i in range(1, 13):
        if month[i]:
            break
    calc(0, i)
    # calc(0, 1)
    print('#{} {}'.format(tc, min_cost))

