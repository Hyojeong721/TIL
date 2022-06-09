# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
# 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.

import sys
sys.stdin = open('input.txt')

def next_search(s, f):
    global cnt, arr
    cnt += 1

    # 리스트에서 종료시간 빠른 순 찾기
    s = arr[0][0]
    f = arr[0][1]

    for i in range(len(arr)):
        if arr[i][1] < f:
            s = arr[i][0]
            f = arr[i][1]

    # 종료시간보단 빠른 시작시간 리스트 삭제
    index = []
    for j in range(len(arr)):
        if f > arr[j][0]:
            index.append(j)

    for l in reversed(index):
        arr.pop(l)

    if arr:
        next_search(s, f)

    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    next_search(0, 0)

    print("#{} {}".format(tc, cnt))