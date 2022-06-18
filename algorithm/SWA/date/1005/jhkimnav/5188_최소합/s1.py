import sys
sys.stdin = open('input.txt')


def dfs(s, total):
    global min_total

    if s[0] not in range(N) or s[1] not in range(N):
        return

    if total > min_total:
        return

    if s[0] == N-1 and s[1] == N-1:

        total += arr[s[0]][s[1]]

        if total < min_total:
            min_total = total
        return

    else:
        total += arr[s[0]][s[1]]
        dfs([s[0], s[1] + 1], total)
        dfs([s[0] + 1, s[1]], total)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N

    for i in range(N):
        arr[i] = list(map(int, input().split()))

    start = [0, 0]
    min_total = N * N * 10
    total = 0

    dfs(start, total)

    print('#{} {}'.format(tc, min_total))
