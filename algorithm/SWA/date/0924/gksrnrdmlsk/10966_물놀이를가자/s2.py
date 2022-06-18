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
                        queue.append([r + dx[i], c + dy[i], 1])
    start = 0
    end = len(queue)
    if end == 0:
        print('#{} {}'.format(tc, answer))
        break
    queue = queue + [0] * 100
    while start < end:
        curr = queue[start]
        for i in range(4):
            if lst[curr[0] + dx[i]][curr[1] + dy[i]] == 'L':
                queue[end] = [curr[0] + dx[i], curr[1] + dy[i], curr[2] + 1]
                answer += curr[2] + 1
                lst[curr[0] + dx[i]][curr[1] + dy[i]] = curr[2] + 1
                end += 1
        start += 1
    print(queue)

    print('#{} {}'.format(tc, answer))









    #             stack.append([r, c, 1000])
    # target = len(stack)
    # cnt = 0
    # stat = 1
    # for i in stack:
    #     for j in range(4):
    #         if lst[i[0] + dx[j]][i[1] + dy[j]] == 'W':
    #             i = [i[0], i[1], 1]
    #             lst[i[0]][i[1]] = 1
    #             cnt += 1
    #             answer += 1
    #
    # while cnt < target:
    #     stat += 1
    #     for i in stack:
    #         if i[2] > stat:
    #             for j in range(4):
    #                 if lst[i[0] + dx[j]][i[1] + dy[j]] == stat - 1:
    #
    #
    #
    #
    # print('#{} {}'.format(tc, answer))