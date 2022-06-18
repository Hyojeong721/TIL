import sys
sys.stdin = open("input.txt")
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(N-1):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < 5 and 0 <= nc < 5:
                    diff = N_list[nr][nc] - N_list[i][j]
                    if diff < 0:
                        diff = -diff
                    total += diff
    print('#%d %d' % (t, total))


