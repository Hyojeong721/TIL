import sys
sys.stdin = open('input.txt')
T = int(input())


def when_find(total, target):
    num = 0
    left = 1
    right = total

    if target == left or target == right:
        return num

    while left <= right:
        c = int((left + right) / 2)
        num += 1
        if c == target:
            return num
        elif c > target:
            right = c
        else:
            left = c


for tc in range(1, T+1):
    info = list(map(int, input().split()))
    a = when_find(info[0], info[1])
    b = when_find(info[0], info[2])
    if a < b:
        result = 'A'
    elif b < a:
        result = 'B'
    else:
        result = '0'

    print(f'#{tc} {result}')
