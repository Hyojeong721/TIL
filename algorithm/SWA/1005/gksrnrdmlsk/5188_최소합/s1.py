import sys
sys.stdin = open('input.txt')

dx = [0, 1]
dy = [1, 0]

def searching(r, c, total):
    global answer
    if r == N -1 and c == N - 1:
        if total < answer:
            answer = total
        return
    elif total < answer:
        for i in range(2):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < N:
                searching(nr, nc, total + numbers[nr][nc])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    answer = 300
    searching(0, 0, numbers[0][0])
    print('#{} {}'.format(tc, answer))

