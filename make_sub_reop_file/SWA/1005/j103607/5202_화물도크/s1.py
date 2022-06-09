import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    temp = [list(map(int, input().split())) for _ in range(N)]

    '''
    # 버블소트
    for i in range(N-1):
        for j in range(N-i-1):
            if schedule[j][1] > schedule[j+1][1]:
                schedule[j], schedule[j+1] = schedule[j+1], schedule[j]
    '''
    schedule = sorted(temp, key=lambda x: x[1])   # 끝나는 시점을 기준으로 정렬

    count = 1
    now = schedule.pop(0)   # now: 현재 작업
    for i in range(N-1):
        next = schedule.pop(0)   # next: 다음 작업
        if now[1] <= next[0]:   # 작업 끝나는 시점이 다음 작업 시작 시점보다 빠르면 카운트증가 + 다음 작업이 현재 작업이 됨
            count += 1
            now = next

    print('#{} {}'.format(tc, count))