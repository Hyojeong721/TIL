# tc 8/10개
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
        temp = now + K  # temp에 이동 먼저 해놓고 밑에 테스트

        for i in range(K):
            # 이동한 정류장이 충전정류장리스트에 있는가?
            if temp in charge_spot:
                # 있다면 현재위치로 확정 / 충전횟수 +1
                now = temp
                cnt += 1
                break
            # 충전 안되는 위치라면 없으면 temp-1(K번 반복) 다시 확인
            else:
                temp -= 1
        else:
            cnt = 0
            break
    print("#{} {}".format(tc, cnt))

    # temp 정류장이 충전정류장리스트에 있는가?
    #   없으면 temp-i(i = range(1,k)) 다시 확인
    #   있으면 now = temp 하고 충전횟수 cnt + 1
    #   다시 맨위 while 반복문