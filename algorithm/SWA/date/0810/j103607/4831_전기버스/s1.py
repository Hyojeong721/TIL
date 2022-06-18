import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):
    # K: 한번에 이동가능한 최대 정류장 수
    # N: 종점 정류장 번호
    # M: 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())
    # M: 충전기가 설치된 정류장 번호 리스트
    M = list(map(int, input().split()))

    # 충전기 설치된 정류장(1)이 표시된 리스트
    route = [0]*N
    for i in M:
        route[i] = 1

    count = 0   # 충전 횟수
    v = 0       # 현재 위치(v)
    while v < N-K:
        for j in range(K, 0, -1):
            if route[v+j] == 1:
                count += 1
                v = v+j
                break
        else:
            count = 0
            break

    print('#{} {}'.format(tc, count))