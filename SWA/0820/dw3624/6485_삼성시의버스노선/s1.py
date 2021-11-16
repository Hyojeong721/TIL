import sys
sys.stdin = open('input.txt')

# 문제(예시)
# 1에서 3까지만 다니는 버스1
# 2에서 5까지만 다니는 버스2
# 총 정류장 5개
# 각 정류장은 C
# 각 정류장을 지나는 횟수는?


T = int(input())

for t in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]
    visit = [0] * P
    # print(N, bus)
    # print(C)
    # print(visit)

    for b in bus:
        start = b[0]
        end = b[1]

        # if start > end:
        #     start, end = end, start
        for i in range(len(C)):
            if C[i] >= start and C[i] <= end:
                visit[i] += 1

    result = ''
    for v in visit:
        result += ' ' + str(v)
    print('#{} {}'.format(t, result[1:]))