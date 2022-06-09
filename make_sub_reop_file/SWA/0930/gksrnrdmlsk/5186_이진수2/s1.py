import sys
sys.stdin = open('input.txt')
import math

T = int(input())
for tc in range(1, T + 1):
    number = float(input())
    answer = ''
    for i in range(1, 13):
        if number >= 2 ** (-i):
            number -= 2 ** (-i)
            answer += '1'
        else:
            answer += '0'

    for j in range(11, -1, -1):
        if answer[j] == '1':
            answer = answer[:j+1]
            break

    if math.isclose(number, 0):
        print('#{} {}'.format(tc, answer))
    else:
        print('#{} {}'.format(tc, 'overflow'))