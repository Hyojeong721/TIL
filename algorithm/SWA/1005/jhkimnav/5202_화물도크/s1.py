import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    time_table = [0] * N

    # 시작시간과, 종료시간을 하나의 리스트로 묶어서 저장
    for i in range(N):
        time_table[i] = list(map(int, input().split()))

    # 종료시간을 기준으로 오름차순 정렬
    time_table = sorted(time_table, key=lambda x: x[1])
    # print(time_table)
    work = [[0, 0]]

    # 만약 현재 작업의 시작시간이 제일 마지막에 진행된 작업의 종료시간 이후라면
    # 작업 추가
    for i in range(len(time_table)):
        if work[-1][1] <= time_table[i][0]:
            work.append(time_table[i])

    print('#{} {}'.format(tc, len(work)-1))
