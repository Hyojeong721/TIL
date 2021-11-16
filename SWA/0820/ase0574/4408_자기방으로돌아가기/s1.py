import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 돌아가야 할 학생 수
    N = int(input())
    # 현재방 돌아갈 방
    rooms = [list(map(int, input().split())) for _ in range(N)]
    #
    road = [0] * 201
    for n in range(N):
        # 방번호를 복도 번호로 바꿔주기
        rooms[n][0] = (rooms[n][0]+1) // 2
        rooms[n][1] = (rooms[n][1]+1) // 2

    for i in range(N):
        # 돌아갈 방번호가 더 작은 경우
        if rooms[i][0] > rooms[i][1]:
            rooms[i][0], rooms[i][1] = rooms[i][1], rooms[i][0]
        # 복도 들리는 곳 체크해서 젤 큰수 뽑아내면 그게 답이다!
        for j in range(rooms[i][0], rooms[i][1]+1):
            road[j] += 1

    print("#{} {}".format(tc, max(road)))




