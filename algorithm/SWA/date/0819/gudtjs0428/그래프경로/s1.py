import sys
sys.stdin = open('input.txt')

def if_can_go(V , routes, to_check):
    visited = [0] * (V + 1)
    stack = [to_check[0]]
    routes_remain = routes[:]
    while len(stack):
        current = stack.pop()     # 현재 위치
        i = 0
        while i < len(routes_remain):
            depart = routes_remain[i][0]
            arriv = routes_remain[i][1]
            if current == depart:
                visited[arriv] = 1
                stack.append(arriv)
                del routes_remain[i]
            else:
                i += 1

    if visited[to_check[1]] == 1:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    routes = []
    for _ in range(E):
        routes.append(list(map(int, input().split())))
    to_check = list(map(int, input().split()))
    print('#{} {}'.format(tc, if_can_go(V, routes, to_check)))