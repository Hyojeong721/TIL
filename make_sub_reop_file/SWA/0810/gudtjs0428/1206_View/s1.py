import sys
sys.stdin = open('input.txt')

T = 10

def if_river(houses):
    count = 0
    for i in range(2, len(houses) - 2):
        around_houses = [houses[i-2], houses[i-1], houses[i+1], houses[i+2]]
        max_house = around_houses[0]
        for around_house in around_houses:
            if around_house >= max_house:
                max_house = around_house
        if houses[i] > max_house:
            count += houses[i] - max_house
    return count

for tc in range(1, T + 1):
    input()
    houses = list(map(int, input().split()))
    print('#{} {}'.format(tc, if_river(houses)))