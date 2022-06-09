import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())

    number = list(map(int, input().split()))
    # ev = [0] * (N + 1)       # 충전소는 1   eg. [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    # visited = [0] * (N + 1)  # 방문한 곳은 1, 방문하지 않은 곳은 0   eg. [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #
    # for i in number:
    #     ev[i] = 1
    #
    # now = 0  # 현재 위치 0에서 시작
    # dis = K  # 첫 턴에 최대 이동 가능 거리인 K만큼 이동 시도,
    #          # 이동 시도한 자리에 충전소가 없으면 K -= 1를 하고 다시 이동 시도
    #          # dis가 0이 될 때까지 이동하지 못하면 종료
    # while True:
    #     if now + dis < N:         # 목적지에 도착하지 못한 경우
    #         now += dis
    #         if ev[now] == 1:      # 충전소에 도착한 경우
    #             visited[now] = 1
    #             if dis != K:
    #                 dis = K
    #         else:                 # 충전소에 도착하지 못한한 경우
    #             now = dis
    #             dis -= 1
    #         if dis == 0:          # dis == 0이 되면 더 이상 이동할 수 없으므로 종료
    #             result = 0
    #             break
    #
    #     elif now + dis >= N:      # 목적지에 도착하면 종료
    #         result = sum(visited)
    #         # 끝
    #         break
    # print('#{} {}'.format(tc, result))


    # dis = K
    # now = K
    # while True:
    #     if now >= N:
    #         result = sum(visited)
    #         break
    #     elif ev[now] == 1:
    #         dis = K
    #         visited[now] = 1
    #         now += K
    #     elif ev[now] == 0:
    #         now -= 1
    #         dis -= 1
    #         if dis == 0:
    #             result = 0
    #             break
    # print("#{} {}".format(t, result))

    #
    # ev = [0] * (N+1)
    # for i in number:
    #     ev[i] = 1
    #
    # visited = 0
    # now = 0
    # dis = K
    #
    # while now < N:
    #     if now + K >= N:
    #         break
    #     else:
    #         if ev[now + dis] == 1:
    #             visited += 1
    #             now += dis
    #             dis = K
    #         else:
    #             dis -= 1
    #             if dis == 0:
    #                 visited = 0
    #                 break
    # print('#{} {}'.format(tc, visited))
    cnt = 0
    now = 0
    visit = 0
    while True:
        for i in range(K, -1, -1):
            if i == 0:
                visit = 0
                cnt += 1
                break

            if now + i >= N:
                cnt += 1
                break

            else:
                if now + i in number:
                    now += i
                    visit += 1
                    break

        if cnt == 1:
            break
    print('#{} {}'.format(tc, visit))