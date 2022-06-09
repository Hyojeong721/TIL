import sys
sys.stdin = open('input.txt', 'r')


def find_way(arr):
    if len(arr) == N:
        routes.append(arr[:]+[0])
        return

    for x in range(N):
        if x not in arr:
            arr.append(x)
            find_way(arr)
            arr.remove(x)


def cost(arr):
    total = 0
    for i in range(N):  # 0 ~ n-1
        total += graph[arr[i]][arr[i+1]]
    return total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]
    routes = []
    find_way(visited)
    print(routes)
    minimum = 9876543210

    for route in routes:
        tmp = cost(route)
        if tmp < minimum:
            minimum = tmp

    print(f'#{tc} {minimum}')