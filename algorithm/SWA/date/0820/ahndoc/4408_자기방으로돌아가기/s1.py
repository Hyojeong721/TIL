import sys
sys.stdin = open('input.txt')

# def div(num):
#     return (int(num)+1) // 2

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 돌아갈 사람의 수
    students = [list(map(int, input().split())) for _ in range(N)]

    # 모든 복도 앞을 0으로 설정
    corridor = [0] * 201
    # 복도 앞을 기준으로 순서쌍 재설정
    for i in range(N):
        students[i][0] = (students[i][0] + 1) // 2
        students[i][1] = (students[i][1] + 1) // 2
        # 순서쌍 교체
        if students[i][1] < students[i][0]:
            students[i][0], students[i][1] = students[i][1], students[i][0]
        # 지나간 복도에 모두 1씩 더해줌
        for j in range(students[i][0], students[i][1] + 1):
            corridor[j] += 1

    # 가장 많이 지나간 복도의 값(최대값) 구하기
    max_v = corridor[0]
    for i in corridor:
        if i > max_v:
            max_v = i

    print('#{} {}'.format(tc, max_v))






    #######################################

    # # students = [list(map(int, input().split())) for _ in range(N)]
    # students = [list(map(div, input().split())) for _ in range(N)]
    #
    # road = [0] * 201
    #
    # for i in range(N):
    #     if students[i][0] > students[i][1]:
    #         students[i][0], students[i][1] = students[i][1], students[i][0]
    #
    #     for j in range(students[i][0], students[i][1] + 1):
    #         road[j] += 1
    #
    # print('#{} {}'.format(tc, max(road)))