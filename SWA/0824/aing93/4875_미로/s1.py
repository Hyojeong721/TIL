import sys
sys.stdin = open('input.txt')

#상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    n = len(arr)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                y, x = i ,j
    stack = [[y, x]]
    print(stack)
    while stack:
        y,x = stack.pop()
        arr[y][x] = 1
        for i in range(4):
            y = y+dy[i]
            x = x+dy[i]


