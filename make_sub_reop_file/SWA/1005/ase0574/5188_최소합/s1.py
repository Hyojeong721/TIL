import sys
sys.stdin = open('input.txt')
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때,
# 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램

def road(x, y, total):
    global result, dx, dy

    if x == N-1 and y==N-1:
        total += arr[y][x]
        if total < result:
            result = total
            return
    if total > result:
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if x > N-1 or y > N-1:
            continue
        if not visited[y][x]:
            visited[y][x] = 1
            road(nx, ny, total+arr[y][x])
            visited[y][x]=0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited=[[0 for _ in range(N)] for _ in range(N)]
    result = 10*2*N

    # 오른쪽, 아래로만 이동가능
    dx = [+1, 0]
    dy = [0, +1]

    road(0, 0, 0)

    print("#{} {}".format(tc, result))