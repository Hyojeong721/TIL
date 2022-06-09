'''
    list 사용, 가지치기용 배열 -> Fail (제한시간 초과) - 3개 맞음
        77,636 kb / 8,006 ms / 757 lines

    set 사용 -> Pass
        71,924 kb / 484 ms / 684 lines
'''
import sys
sys.stdin = open('input.txt')


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def make_number(r, c, number):
    global visited, numbers
 
    if len(number) == 7:
        # if number not in numbers:
        #     numbers.append(number)
        numbers.add(number)
        return

    number += board[r][c]
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            make_number(nr, nc, number)


T = int(input())
for tc in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]

    # numbers =[]
    numbers = set()
    for r in range(4):
        for c in range(4):
            make_number(r, c, '')
    print('#{} {}'.format(tc, len(numbers)))