import sys
sys.stdin = open('input.txt')

def search(curr, cost):
    global answer
    if cost >= answer:
        return
    else:
        if curr == N:
            if cost < answer:
                answer = cost
        else:
            for i in range(N):
                if visited[i] == 0:
                    visited[i] = 1
                    search(curr + 1, cost + lst[curr][i])
                    visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input(). split())) for _ in range(N)]
    visited = [0] * N
    answer = 100 * N
    search(0, 0)
    print('#{} {}'.format(tc, answer))