import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    answer = 0
    N, M = map(int, input().split())
    lst = [[-1] * (M + 2)] + [[-1] + list(input()) + [-1] for _ in range(N)] + [[-1] * (M + 2)]
    queue = []
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if lst[r][c] == 'W':
                for i in range(4):
                    if lst[r + dx[i]][c + dy[i]] == 'L':
                        lst[r + dx[i]][c + dy[i]] = 1
                        answer += 1
                        queue.append((r + dx[i], c + dy[i]))
    start = 0
    end = len(queue)
    queue = queue + [0] * (M * N)

    if end != 0:
        while start != end:
            curr = queue[start]
            for i in range(4):
                if lst[curr[0] + dx[i]][curr[1] + dy[i]] == 'L':
                    queue[end] = (curr[0] + dx[i], curr[1] + dy[i])
                    lst[curr[0] + dx[i]][curr[1] + dy[i]] = lst[curr[0]][curr[1]] + 1
                    answer += lst[curr[0]][curr[1]] + 1
                    end += 1
            start += 1

    print('#{} {}'.format(tc, answer))

