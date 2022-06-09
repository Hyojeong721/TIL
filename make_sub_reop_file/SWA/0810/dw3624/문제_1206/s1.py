import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    num = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(num - 5 + 1):
        tmp = buildings[i:i+5]
        a = tmp[2] - tmp[0]
        b = tmp[2] - tmp[1]
        c = tmp[2] - tmp[3]
        d = tmp[2] - tmp[4]
        height_diff = [a, b, c, d]

        if a > 0 and b > 0 and c > 0 and d > 0:
            min_diff = a
            for diff in height_diff:
                if diff < min_diff:
                    min_diff = diff
            result += min_diff

    print('#{} {}'.format(t, result))