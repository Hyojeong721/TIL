# 실패

import sys
sys.stdin = open('input.txt')

def searching(N, prob, cand):
    global answer
    left = len(cand)
    if prob < answer:
        return
    else:
        if not cand:
            if prob > answer:
                answer = prob
        else:
            for i in cand:
                cand.remove(i)
                searching(N, prob * lst[N - left][i], cand)
                cand.add(i)

def normalize(string):
    return int(string) / 100

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(normalize, input().split())) for _ in range(N)]
    answer = 0
    searching(N, 1, set(range(N)))
    print('#{} {:f}'.format(tc, answer * 100))




# def searching(N, prob, cand):
#     global answer
#     left = len(cand)
#     if prob < answer:
#         return
#     else:
#         if not cand:
#             if prob > answer:
#                 answer = prob
#         else:
#             for i in cand:
#                 cand.remove(i)
#                 searching(N, prob * lst[N - left][i], cand)
#                 cand.add(i)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     answer = 1
#     for i in range(N):
#         answer *= lst[i][i]
#     searching(N, 1, set(range(N)))
#     print('#{} {:f}'.format(tc, answer / (100 ** (N - 1))))