import sys
sys.stdin = open('input.txt')

T = int(input())

def count_charge(K, N, stops):
    count = 0
    # 지나칠 충전정거장
    passby = []
    # 출발한 정거장
    prestop = 0
    for i in range(len(stops)):
        # 다음 충전정거장
        nextstop = stops[i]
        # 출발한 정거장에서 종점까지 도착할 수 있을 경우
        if prestop + K >= N:
            return count
        # 가야할 정거장이 지나칠 충전정거장이거나 이미 도착한 정거장일 경우
        if nextstop in passby or nextstop == prestop:
            continue
        # 가야할 충전정거장에 도달할 수 없을 경우
        if nextstop - prestop > K:
            return 0
        # 다음 충전정거장에 도착할 수 있는 경우
        elif nextstop - prestop <= K:
            # 그 뒤 충전정거장들에 도달할 수 있는지 확인하기 위해 temp 설정
            temp = stops[i:]
            for j in range(len(temp)):
                # 마지막 충전정거장에서 다음을 찾게 되는 경우 에러가 발생할 경우를 우려해 try 사용
                try:
                    # 충전된 전기로 j+1번째 충전정거장까지 갈 수 없는 경우
                    if temp[j+1] - prestop > K:
                        count += 1
                        # 현재 정거장을 j번째 정거장으로 설정
                        prestop = temp[j]
                        break
                    else:
                        # 충전된 전기로 j+1번째 충전정거장까지 갈 수 있는 경우 j번째 정거장은 지나칠 정거장에 등록
                        passby.append(temp[j])
                # 마지막 충전정거장까지 왔으나 전기가 남았을 시
                except:
                    # 출발한 정거장에서 종점까지 도달할 수 있는 경우
                    if N - prestop <= K:
                        return count
                    else:
                        prestop = temp[j]
                        count += 1
                        if N - prestop <= K:
                            return count
                        else:
                            return 0

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    print('#{0} {1}'.format(tc, count_charge(K, N, stops)))