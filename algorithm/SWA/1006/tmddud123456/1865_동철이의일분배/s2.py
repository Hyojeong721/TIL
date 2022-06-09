import sys
sys.stdin = open('input.txt')

def searching(N, prob, cand):
    global answer
    if prob <= answer:
        return
    else:
        if cand == N:
            if prob > answer:
                answer = prob
            return
        else:
            for i in range(N):
                if visited[i] == 0:
                    visited[i] = 1
                    searching(N, prob * lst[cand][i], cand+1)
                    visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(lambda a: int(a)/100, input().split())) for _ in range(N)]
    answer = 0
    visited = [0] * N
    searching(N, 1, 0)
    print('#{} {:f}'.format(tc, answer * 100))