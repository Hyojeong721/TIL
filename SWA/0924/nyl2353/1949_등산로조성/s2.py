"""
s1 수정
"""
import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_longest(r, c, distance):
    global longest, repair

    if distance > longest:
        longest = distance

    visited[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]: continue

        # 낮을 때
        if mountain[nr][nc] < mountain[r][c]:
            find_longest(nr, nc, distance + 1)
        # 높거나 같을 때
        else:
            diff = mountain[nr][nc] - mountain[r][c] + 1
            # 공사 할 수 있을 때 (아직 안 했고, K가 충분히 클 때)
            if not repair and diff <= K:
                mountain[nr][nc] -= diff
                repair = True
                find_longest(nr, nc, distance + 1)
                mountain[nr][nc] += diff
                repair = False

    visited[r][c] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = []
    tops = []
    highest = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        mountain.append(temp)
        if max(temp) > highest:
            highest = max(temp)

    longest = 0
    repair = False
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == highest:
                find_longest(r, c, 1)

    print('#{} {}'.format(tc, longest))