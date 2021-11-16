# pass 성공
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    #K:이동할 수 있는 최대 정류장 수 N:종점 M:총 충전소 수
    K, N, M = map(int, input().split())
    charge_spot = list(map(int, input().split()))

    now = 0
    cnt = 0
    # temp + k > N 넘으면 break
    while now + K < N:
        for i in range(K, 0, -1):
            # 이동할 정류장이 충전소인가?
            if (now + i) in charge_spot:
                # 충전소라면 현재위치를 이동 / 충전횟수 +1
                now += i
                cnt += 1
                break
            # 이동할 정류장이 충전소가 아니면 -1씩 되돌아가서 확인

        else: # 이동할 정류장이 모두 충전소가 아니면 잘못된 케이스
            cnt = 0
            break

    print("#{} {}".format(tc, cnt))
