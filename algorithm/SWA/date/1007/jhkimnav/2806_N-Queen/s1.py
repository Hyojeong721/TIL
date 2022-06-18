import sys
sys.stdin = open('input.txt')


def dfs(i):
    global ans

    if i == N:
        ans += 1
        return

    else:
        for j in range(N):
            if not visited[j] and not arr[i][j]:
                # i = 0
                # j = 3
                visited[j] = 1
                arr[i][j] = 1

                # 대각선 오른쪽 아래
                y = 1
                x = 1
                while y in range(N-i) and x in range(N-j):
                    arr[i+y][j+x] += 1
                    y += 1
                    x += 1

                # 대각선 왼쪽 위 O
                y = -1
                x = -1
                while i+y in range(N) and j+x in range(N):
                    arr[i+y][j+x] += 1
                    y -= 1
                    x -= 1

                # 대각선 오른쪽 위(0)
                y = -1
                x = 1
                # print('{}, {}'.format(i, j))
                while i+y in range(N) and j+x in range(N):
                    arr[i+y][j+x] += 1
                    y -= 1
                    x += 1

                # 대각선 왼쪽 아래 O
                y = 1
                x = -1
                while i+y in range(N) and j+x in range(N):
                    arr[i+y][j+x] += 1
                    y += 1
                    x -= 1

                # for i in range(N):
                #     print(arr[i])
                # print()
                dfs(i+1)
                arr[i][j] = 0
                visited[j] = 0


##################################################################################
                # 대각선 오른쪽 아래
                y = 1
                x = 1
                while y in range(N-i) and x in range(N-j):
                    arr[i+y][j+x] -= 1
                    y += 1
                    x += 1

                # 대각선 왼쪽 위 O
                y = -1
                x = -1
                while i+y in range(N) and j+x in range(N):
                    arr[i+y][j+x] -= 1
                    y -= 1
                    x -= 1

                # 대각선 오른쪽 위(0)
                y = -1
                x = +1
                while i+y in range(N) and j+x in range(N):
                    arr[i+y][j+x] -= 1
                    y -= 1
                    x += 1

                # 대각선 왼쪽 아래 O
                y = 1
                x = -1
                while i+y in range(N) and j+x in range(N):
                    arr[i+y][j+x] -= 1
                    y += 1
                    x -= 1

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    ans = 0
    visited = [0] * N

    dfs(0)
    print('#{} {}'.format(tc, ans))


