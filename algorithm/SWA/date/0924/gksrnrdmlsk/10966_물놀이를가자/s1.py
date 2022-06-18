import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [[-1] * (M + 2)] + [[-1] + list(input()) + [-1] for _ in range(N)] + [[-1] * (M + 2)]
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if lst[r][c] == 'L':
                queue = [[[r, c, 0]]]
                while queue:
                    curr = queue.pop(0)
                    for i in range(4):
                        if lst[curr[-1][0] + dx[i]][curr[-1][1] + dy[i]] == 'W':
                            for j in curr:
                                lst[j[0]][j[1]] = curr[-1][2] + 1 - j[2]
                            queue = []
                            break

                        elif lst[curr[-1][0] + dx[i]][curr[-1][1] + dy[i]] not in ('L', -1):
                            for k in range(i, 4):
                                if lst[curr[-1][0] + dx[k]][curr[-1][1] + dy[k]] == 'W':
                                    for j in curr:
                                        lst[j[0]][j[1]] = curr[-1][2] + 1 - j[2]
                                        queue = []
                                    break
                            if lst[curr[-1][0]][curr[-1][1]] == 'L':
                                for j in curr:
                                    lst[j[0]][j[1]] = lst[curr[-1][0] + dx[i]][curr[-1][1] + dy[i]] + curr[-1][2] + 1 - j[2]
                                    queue = []
                                break

                        elif lst[curr[-1][0] + dx[i]][curr[-1][1] + dy[i]] == -1:
                            pass

                        else:

                            queue.append(curr + [[curr[-1][0] + dx[i], curr[-1][1] + dy[i], curr[-1][2] + 1]])
                            print(queue)
    answer = 0
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if lst[r][c] not in ('W', 'L'):
                answer += lst[r][c]

    print('#{} {}'.format(tc, answer))