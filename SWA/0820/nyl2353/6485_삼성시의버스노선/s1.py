import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 5000개의 버스정류장 존재
    stations = [0 for _ in range(5001)]
    # 출력할 문자열
    result = '#{}'.format(tc)

    N = int(input())
    for n in range(N):
        A, B = list(map(int, input().split()))
        for route in range(A, B + 1):
            stations[route] += 1

    P = int(input())
    for p in range(P):
        C = int(input())
        result += ' {}'.format(stations[C])

    print(result)