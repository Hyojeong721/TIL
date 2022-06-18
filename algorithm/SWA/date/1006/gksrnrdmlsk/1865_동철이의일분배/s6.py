# 성공. 민수님 감사합니다,,,

import sys
sys.stdin = open('input.txt')

def searching(N, prob, phase):
    global answer
    if prob * (100 ** (N - phase)) <= answer:
        return
    else:
        if phase == N:
            if prob > answer:
                answer = prob
            return
        else:
            for i in range(N):
                if visited[i] == 0:
                    visited[i] = 1
                    searching(N, prob * lst[phase][i], phase+1)
                    visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    visited = [0] * N
    searching(N, 1, 0)
    print('#{} {:f}'.format(tc, answer * (100 ** (-N + 1))))