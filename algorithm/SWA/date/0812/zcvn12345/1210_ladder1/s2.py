import sys
sys.stdin = open('input.txt')

T = 10

def status(arr, i, j, state):
    if state == 'up':
        if j > 0 and arr[i][j-1] == 1:
            return 'left'
        elif j < 99 and arr[i][j+1] == 1:
            return 'right'
        else:
            return 'up'
    if state == 'left':
        if arr[i-1][j] == 1:
            return 'up'
        else:
            return 'left'

    if state == 'right':
        if arr[i-1][j] == 1:
            return 'up'
        else:
            return 'right'



for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(100)]
    now_x = 0
    now_y = 0
    for i in range(100):
        for j in range(100):
            if matrix[i][j] == 2:
                now_x = i
                now_y = j
    state = 'up'
    while now_x > 0:
        if state == 'up':
            now_x -= 1
            state = status(matrix, now_x, now_y, state)
        elif state == 'left':
            now_y -= 1
            state = status(matrix, now_x, now_y, state)
        elif state == 'right':
            now_y += 1
            state = status(matrix, now_x, now_y, state)
    print('#{0} {1}'.format(test_case, now_y))