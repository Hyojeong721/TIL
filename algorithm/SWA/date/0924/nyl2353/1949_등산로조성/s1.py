import sys
sys.stdin = open('input.txt')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_longest(start, distance):
    global longest, repair, visited

    r = start[0]
    c = start[1]
    for k in range(4):
        row = r + dr[k]
        col = c + dc[k]
        if 0 <= row < N and 0 <= col < N and not visited[row][col]:
            # 낮을 때
            if mountain[row][col] < mountain[r][c]:
                visited[row][col] = True
                find_longest([row, col], distance + 1)
                visited[row][col] = False
            # 높거나 같을 때
            else:
                diff = mountain[row][col] - mountain[r][c] + 1
                # 공사 할 수 있을 때 (아직 안 했고, K가 충분히 클 때)
                if not repair and diff <= K:
                    mountain[row][col] -= diff
                    repair = True
                    visited[row][col] = True
                    find_longest([row, col], distance + 1)
                    mountain[row][col] += diff
                    repair = False
                    visited[row][col] = False

        # 더 갈 데 없을 때, 최대길이와 비교
        elif longest < distance:
            longest = distance


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
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == highest:
                tops.append([r, c])

    longest = 0
    repair = False
    visited = [[False] * N for _ in range(N)]
    for top in tops:
        visited[top[0]][top[1]] = True
        find_longest(top, 1)
        visited[top[0]][top[1]] = False

    print('#{} {}'.format(tc, longest))