import sys
sys.stdin = open('input.txt')

def searching(recent, total, left):
    global answer
    if total > answer:
        return

    elif not left:
        total += numbers[recent][0]
        if total < answer:
            answer = total
    else:
        for i in left:
            searching(i, total + numbers[recent][i], left - {i,})

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    answer = 10000
    searching(0, 0, set(range(1, N)))
    print('#{} {}'.format(tc,answer))
