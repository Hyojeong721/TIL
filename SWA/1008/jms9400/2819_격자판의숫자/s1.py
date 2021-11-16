import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(i, j, a, num):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    if a >= 7:
        if num not in answer:
            answer.append(num)
        return

    for n in range(4):
        x = i + dx[n]
        y = j + dy[n]

        if x in range(4) and y in range(4):
            dfs(x, y, a+1, num + arr[x][y])


for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    answer = []

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, arr[i][j])

    print('#{} {}'.format(tc, len(answer)))