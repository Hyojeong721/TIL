import sys
sys.stdin = open('input.txt')
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
tunnel = {1: (0, 1, 2, 3),
          2: (1, 3),
          3: (0, 2),
          4: (0, 3),
          5: (0, 1),
          6: (1, 2),
          7: (2, 3),
          }

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    lst = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]
    visited = [[0] * (M + 2) for _ in range(N + 2)]
    queue = [(R + 1, C + 1, 0)]
    while queue:
        curr = queue.pop(0)
        if curr[2] >= L:
            break
        visited[curr[0]][curr[1]] = 1
        for i in tunnel[lst[curr[0]][curr[1]]]:
            if lst[curr[0] + dx[i]][curr[1] + dy[i]] != 0 and visited[curr[0] + dx[i]][curr[1] + dy[i]] == 0:
                if (i + 2) % 4 in tunnel[lst[curr[0] + dx[i]][curr[1] + dy[i]]]:
                    queue.append((curr[0] + dx[i], curr[1] + dy[i], curr[2] + 1))
    answer = 0
    for i in visited:
        answer += sum(i)
    print('#{} {}'.format(tc, answer))

