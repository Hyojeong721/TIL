import sys
sys.stdin = open('input.txt')
#
# T = int(input())

for test_case in range(1, 11):
    width = int(input())
    buildings = list(map(int, input().split()))
    total = 0
    for building in range(2, len(buildings)-2):
        temp = 0
        if buildings[building-2] > buildings[building-1]:
            left = buildings[building-2]
        else:
            left = buildings[building-1]

        if buildings[building+2] > buildings[building+1]:
            right = buildings[building+2]
        else:
            right = buildings[building+1]

        if left > right:
            temp = buildings[building] - left
        else:
            temp = buildings[building] - right

        if temp > 0:
            total += temp
        else:
            pass

    print('#{0} {1}'.format(test_case, total))

