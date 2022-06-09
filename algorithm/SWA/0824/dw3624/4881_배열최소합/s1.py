# backtracking
import sys
sys.stdin = open('input.txt')


def back(y):
    global tmp, result

    # 계산 중인 합이 지난 합보다 큰 경우
    if tmp > result:
         return

    # 마지막 줄인 경우
    if y == N:
        if tmp < result:
            result = tmp
            return

    # 다음 줄로
    for x in range(N):
        if visit[x] == 0:
            visit[x] = 1
            tmp += mat[y][x]

            back(y + 1)

            visit[x] = 0
            tmp -= mat[y][x]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    tmp, result = 0, 999

    back(0)
    print('#{} {}'.format(t, result))