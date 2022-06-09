import sys
sys.stdin = open('input.txt')

T = int(input())
# 버스노선
for tc in range(1, T+1):
    N = int(input())
    stations = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for bus in range(A, B+1):
            stations[bus] += 1
    P = int(input())
    print('#{0}'.format(tc), end=' ')
    for j in range(P):
        print(stations[int(input())], end=' ')
    print()