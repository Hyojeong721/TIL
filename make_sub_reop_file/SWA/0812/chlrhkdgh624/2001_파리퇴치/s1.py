import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 배열 크기, 파리채 크기

    arr = [list(map(int, input().split())) for _ in range(N)]

    dead_fly = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for di in range(M):
                for dj in range(M):
                    total += arr[i + di][j + dj]
            dead_fly.append(total)

    for k in range(len(dead_fly), 0, -1):
        for h in range(0, k-1):
            if dead_fly[h] > dead_fly[h+1]:
                dead_fly[h], dead_fly[h+1] = dead_fly[h+1], dead_fly[h]

    print(f'#{tc} {dead_fly[-1]}')
