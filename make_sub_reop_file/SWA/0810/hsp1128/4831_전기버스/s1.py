import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    #K:이동할 수 있는 최대 정류장 수 N:종점 M:총 충전 수
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))
    now = 0
    cnt = 0

    for i in range(0,M):
        #현 지점에서 한번에 종점에 갈 수 있는 경우
        if now + K  >= N:
            break

        else:
            #도착할 수 없는 경우
            if bus_stop[i] - now > K:
                cnt = 0
                break

            #현 지점에서 다음 충전소로 갈 수 있는 경우
            for j in range(M-1, -1, -1):
                if 0 <bus_stop[j] - now <= K:
                    cnt += 1
                    now = bus_stop[j]
                    break




    print('#{} {}'.format(tc, cnt))