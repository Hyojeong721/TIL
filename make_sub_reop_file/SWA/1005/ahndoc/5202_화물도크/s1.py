import sys
sys.stdin = open('input.txt')

def find(schedule):
    global cnt

    finish_time = 0
    for i in range(len(schedule)):
        if schedule[i][0] >= finish_time:
            finish_time = schedule[i][1]
            cnt += 1

# [[4, 14], [8, 18], [17, 20], [20, 23], [23, 24]]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    check = list(range(24))
    visited = [0] * N
    cnt = 0
    schedule.sort(key=lambda x:x[1])

    find(schedule)
    # print(schedule)
    print('#{} {}'.format(tc, cnt))
    # print(schedule)
    # print(check)
