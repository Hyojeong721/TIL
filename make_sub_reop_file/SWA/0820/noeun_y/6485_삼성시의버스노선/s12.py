import sys
sys.stdin= open("input.txt")
def busnum_for_stops(routes, C):
    buses_for_stops = [0] * 5001
    answer = []
    for route in routes:
        for stop in range(route[0], route[1] + 1):
            buses_for_stops[stop] += 1
    for stop in C:
        answer.append(buses_for_stops[stop])
    return answer


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    routes = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))
    print('#{}'.format(test_case), end='')
    for n in busnum_for_stops(routes, C):
        print('', n, end='')

    print("")