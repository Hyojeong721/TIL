import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    start = input()

    # 레이저 개수 (laser_num)
    laser_num = start.count('()')

    # 쇠막대기 개수 (bar_num)
    bar_num = 0
    for i in range(len(start)-1):
        if start[i] == '(' and start[i+1] != ')':
            bar_num += 1

