# 실패

import sys
sys.stdin = open('input.txt')

def searching(N, prob, cand):
    global answer
    left = len(cand)

    if prob * (100 ** left) < answer:
        return
    else:
        if not cand:
            if prob > answer:
                answer = prob
        else:
            for i in list(cand)[:]:
                searching(N, prob * lst[N - left][i], cand - {i,})

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    answer = 1
    for i in range(N):
        answer *= lst[i][i]
    searching(N, 1, set(range(N)))
    print('#{} {:f}'.format(tc, answer / (100 ** (N - 1))))