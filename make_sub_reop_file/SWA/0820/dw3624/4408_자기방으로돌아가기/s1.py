import sys
sys.stdin = open('input.txt')

# idea
# 방번호 list를 복도 idx로 변환
# 출발부터 도착까지, 복도 list의 해당 idx값에 1 추가
# 가장 큰 값 = 최소 소요 단위시간


T = int(input())

def div(num):
    """
    각 방 번호를 복도 인덱스로 변환합니다.
    """
    return (int(num) + 1) // 2


for t in range(1, T+1):
    n = int(input())
    students = [list(map(div, input().split())) for _ in range(n)]
    corridor = [0] * 201
    # print(students)

    for student in students:
        # 출발 방번호가 도착 방번호보다 클 경우 교환
        if student[0] > student[1]:
            student[0], student[1] = student[1], student[0]

        # 출발 방번호부터 도착 방번호까지 복도 list에 1 추가
        ## 복도 list 중 가장 큰 값 = 모두 이동 가능한 최소 단위시간
        for i in range(student[0], student[1] + 1):
            corridor[i] += 1

    result = 0
    for c in corridor:
        if result < c:
            result = c

    print('#{} {}'.format(t, result))