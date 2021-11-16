# 실패

import sys
sys.stdin = open('input.txt')

def searching(prob, cand):
    global answer
    left = len(cand)
    if prob < answer:
        return
    else:
        if not cand:
            if prob > answer:
                answer = prob
        else:
            for i in cand.copy():
                cand.remove(i)
                searching(prob * lst[N - left][i], cand)
                cand.add(i)

def normalize(string):
    return int(string) / 100

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(normalize, input().split())) for _ in range(N)]
    answer = -1
    searching(1, set(range(N)))
    print(lst)
    print('#{0} {1:0.6f}'.format(tc, answer * 100))

