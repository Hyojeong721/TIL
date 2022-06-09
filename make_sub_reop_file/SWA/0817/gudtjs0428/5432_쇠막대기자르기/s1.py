import sys
sys.stdin = open('input.txt')

def count_sticks(laser_and_sticks):
    count = 0
    sticks = 0
    lasers_position = []
    for i in range(1, len(laser_and_sticks)):
        if laser_and_sticks[i] == ')' and laser_and_sticks[i - 1] == '(':
            lasers_position.append(i-1)
    for i in range(len(lasers_position)):
        count += (lasers_position[i] - len(lasers_position[:i+1])) // 2
    sticks = (len(laser_and_sticks) // 2 - len(lasers_position)) + count
    return sticks


T = int(input())
for tc in range(1, T + 1):
    laser_and_sticks = input()
    print('#{} {}'.format(tc, count_sticks(laser_and_sticks)))