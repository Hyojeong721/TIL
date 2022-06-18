# runtime error
# => 10개 중 다섯개...
import sys
sys.stdin = open('input.txt')


def div(num):
    return (int(num)+1) // 2


T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 학생수
    students = [list(map(div, input().split())) for _ in range(N)]  # 출발지 + 목적지
    # print(students)
    cnt = 0  # 단위 시간
    escaped = []  # 도착한 학생 목록

    while N > 0:
        extent = [0] * 201  # 복도
        cnt += 1  # 단위 시간 +1
        for student in students:
            start, end = student[0], student[1]  # 출발/목적지 정보

            if start > end:  # 출발지가 목적지 보다 큰 경우 두 지점 좌표를 변경
                start, end = end, start

            if student in escaped:  # 이미 방에 들어간 학생이라면 패스
                continue

            if 1 in extent[start: end+1]:
                pass
            else:
                for i in range(start, end):
                    extent[i] = 1
                escaped.append(student)
                N -= 1
        else:
            extent = [0] * 201

    print(f'#{tc} {cnt}')


