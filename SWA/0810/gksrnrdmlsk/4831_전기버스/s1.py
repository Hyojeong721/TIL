import sys
sys.stdin = open('input.txt')

T = int(input()) # 몇 번의 테스트 케이스가 있을지 입력받습니다.
for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    lst = sorted(list(map(int, input().split()))) # 쓰면 안 되지만 핵심이 아니라서 그냥 썼습니다... 혹시 몰라서...
    charging = 0 # 마지막으로 충전한 충전소입니다.
    count = 0 # 충전횟수를 가리킵니다.

    while charging < N - K: # N-K 이상이면 그 다음에 빠져나갈 수 있기 때문에 N-K 미만까지 반복합니다. New Keynesian
        count += 1 # 충전할 때마다 한 번씩 올라갑니다.
        for j in range(charging+K, charging, -1): # 최소한으로 충전하기 위해 큰 숫자부터 range를 구성합니다.
            if j in lst: # 갈 수 있는 충전소 중 가장 멀리 있는 충전소를 찾습니다.
                charging = j
                break

        if count > N: # 갈 수 있는 충전소를 가지 못했을 때 while문에서 탈출하기 위해 조건을 만듭니다.
            print('#{} 0'.format(tc)) # 갈 수 있는 충전소를 못 찾았을 때 0을 출력합니다.
            break

    if count <= N: # 목적지 도착 시 충전 횟수를 출력합니다.
        print('#{0} {1}'.format(tc, count))