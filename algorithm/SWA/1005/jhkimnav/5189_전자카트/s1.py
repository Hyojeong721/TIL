import sys
sys.stdin = open('input.txt')


def dfs(s, total):
    global min_cost
    if sum(visited) == N-1:
        print('도착')
        total += arr[s][0]
        if min_cost > total:
            min_cost = total
        return

    else:
        for i in range(1, N):
            if i != s and visited[i] == 0:
                print(s, i)
                visited[i] = 1
                total += arr[s][i]
                # print(total)
                print('재귀 호출 전 i: {},  visited: {}'.format(i, visited))
                dfs(i, total)
                visited[i] = 0
                total -= arr[s][i]
                # print('재귀 호출 후 i: {} , visited{}'.format(i, visited))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    visited = [0] * N

    for n in range(N):
        arr[n] = list(map(int, input().split()))

    start = 0
    cost = 0
    stack = []
    min_cost = 100 * N
    dfs(start, cost)
    print('#{} {}'.format(tc, min_cost))

