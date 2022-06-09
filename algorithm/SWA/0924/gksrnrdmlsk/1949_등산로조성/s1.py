import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    answer = 0
    lst = [[100] * (N + 2)] + [[100] + list(map(int, input().split())) + [100] for _ in range(N)] + [[100] * (N + 2)]
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            starts = []
            biggest = max([max(row[1:N + 1]) for row in lst[1:N + 1]])
            for x in range(1, N + 1):
                for y in range(1, N + 1):
                    if lst[x][y] == biggest:
                        starts.append((x, y))
            for i in range(1, K + 1):
                lst[r][c] -= i
                for j in starts:
                    queue = [(j[0], j[1], 0)]
                    while queue:
                        curr = queue.pop(0)
                        for direction in range(4):
                            if lst[curr[0] + dx[direction]][curr[1] + dy[direction]] < lst[curr[0]][curr[1]]:
                                queue.append((curr[0] + dx[direction], curr[1] + dy[direction], curr[2] + 1))
                    if curr[2] > answer:
                        answer = curr[2]
                lst[r][c] += i

    print('#{} {}'.format(tc, answer + 1))



