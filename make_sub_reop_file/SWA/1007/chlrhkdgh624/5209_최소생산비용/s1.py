import sys
sys.stdin = open('input.txt', 'r')


def backtracking(i, arr, cost):
    global minimum
    if cost > minimum:
        return

    if i == N:
        if cost < minimum:
            minimum = cost
            return
    else:
        for j in range(N):
            if occupied[j]:
                occupied[j] = 0
                arr.append(j)
                backtracking(i+1, arr, cost+info[i][j])
                occupied[j] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    allocated = []
    occupied = [1] * N
    minimum = 99 * N
    current_cost = 0
    backtracking(0, allocated, current_cost)
    print(f'#{tc} {minimum}')