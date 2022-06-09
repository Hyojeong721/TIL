import sys
sys.stdin = open('input.txt')

def if_can_go(routes):
    visited = [0] * 100
    routes_remain = routes[:]
    stack = [0]
    while stack:
        current = stack.pop()
        i = 0
        while i < len(routes_remain):
            start = routes_remain[i][0]
            end = routes_remain[i][1]
            if start == current:
                visited[end] = 1
                stack.append(end)
                routes_remain.remove(routes_remain[i])
            else:
                i += 1

    if visited[99] == 1:
        return 1
    else:
        return 0


T = 10
for tc in range(1, T + 1):
    t, E = map(int,input().split())
    routes_raw = list(map(int, input().split()))
    routes = []
    for i in range(E):
        tmp = [0, 0]
        tmp[0] = routes_raw[i*2]
        tmp[1] = routes_raw[i*2+1]
        routes.append(tmp)
    print('#{} {}'.format(tc, if_can_go(routes)))