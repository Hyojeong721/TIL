import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room_list = [list(map(int, input().split())) for _ in range(N)]

    road = [0] * 401
    max_room = 0

    for i in range(N):
        # 번호가 큰방에서 작은방으로 가는 학생도 있을 수 있음 주의!!
        if room_list[i][0] > room_list[i][1]:
            # temp = room_list[i][1]
            # room_list[i][1] = room_list[i][0]
            # room_list[i][0] = temp
            room_list[i][0], room_list[i][1] = room_list[i][1], room_list[i][0]
        if room_list[i][0] % 2 == 1:
            a = room_list[i][0]
        else:
            a = room_list[i][0] - 1
        if room_list[i][1] % 2 == 1:
            b = room_list[i][1] + 1
        else:
            b = room_list[i][1]

        if b > max_room:
            max_room = b

        for j in range(a, b+1):
            road[j] += 1

    moving_time = 0

    # max road 구하기
    for k in range(1, max_room+1):
        if road[k] > moving_time:
            moving_time = road[k]

    print('#{} {}'.format(tc, moving_time))


# def div(num):
#     return (int(num)+1) // 2
# room_list = [list(map(div, input().split())) for _ in range(N)]

