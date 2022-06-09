# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
# 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.

# 3번째 경우에서 오류 발생 -탐욕알고리즘의
import sys
sys.stdin = open('input.txt')

def next_search(start, finish):
    global cnt

    # 반복 (종료점과 다른활동 시작점 비교)
    next = [99, 99]
    for j in range(N):
        if finish <= arr[j][0]:
            if next[0] >= arr[j][0]:
                next = arr[j]
    cnt += 1
    if next[0] == 99:
        cnt -= 1
    else:
        next_search(next[0], next[1])
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    start = arr[0][0]
    finish = arr[0][1]

    # 스타트 찾기
    for i in range(N):
        if arr[i][0] == start:
            if arr[i][1] < finish:
                start = arr[i][0]
                finish = arr[i][1]
        elif arr[i][0] < start:
            start = arr[i][0]
            finish = arr[i][1]
    cnt += 1

    next_search(start, finish)

    print("#{} {}".format(tc,cnt))