import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def search(r, c, state, length, road):
    global answer, lst

    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if 0 <= nr < N and 0 <= nc < N and lst[r][c] > lst[nr][nc] and (nr, nc) not in road:
            search(nr, nc, state, length + 1, road + [(nr, nc)])

        elif 0 <= nr < N and 0 <= nc < N and state and lst[r][c] > lst[nr][nc] - K and (nr, nc) not in road:
            original = lst[nr][nc]
            lst[nr][nc] = lst[r][c] - 1
            search(nr, nc, 0, length + 1, road + [(nr, nc)])
            lst[nr][nc] = original

    if answer < length:
        answer = length



T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    answer = 0

    lst = []
    peaks = []
    peak_value = 0
    for r in range(N):
        temp = list(map(int, input().split()))
        lst.append(temp)
        for c in range(N):
            if temp[c] < peak_value:
                pass
            elif temp[c] > peak_value:
                peak_value = temp[c]
                peaks = [(r, c)]
            else:
                peaks.append((r, c))

    for r, c in peaks:
        search(r, c, 1, 1, [(r, c)])

    print('#{} {}'.format(tc, answer))

