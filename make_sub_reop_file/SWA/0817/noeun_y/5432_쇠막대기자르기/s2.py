import sys
sys.stdin = open('input.txt')

def count_sticks(laser_and_sticks):
    count = 0
    lasers = 0
    for i in range(1, len(laser_and_sticks)):
        if laser_and_sticks[i] == ')' and laser_and_sticks[i - 1] == '(':
            print(i)
            lasers += 1
            count += laser_and_sticks[:i-1].count('(') - laser_and_sticks[:i-1].count(')')
    sticks = (len(laser_and_sticks) // 2 - lasers) + count
    return sticks


T = int(input())
for tc in range(1, T + 1):
    laser_and_sticks = input()
    #print(laser_and_sticks)
    print('#{} {}'.format(tc, count_sticks(laser_and_sticks)))