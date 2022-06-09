import sys
sys.stdin = open('input.txt')

T = int(input())


def find_road(x, y, a):
    if x == N-1 and y == N-1:
        s.append(a)
        return
    elif x == N-1:
        find_road(x, y+1, a + arr[x][y+1])

    elif y == N-1:
        find_road(x + 1, y, a + arr[x + 1][y])

    elif y+1 in range(N) and x+1 in range(N):
        find_road(x, y+1, a + arr[x][y+1])
        find_road(x+1, y, a + arr[x+1][y])


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    s = []

    find_road(0, 0, arr[0][0])
    print('#{} {}'.format(tc, min(s)))