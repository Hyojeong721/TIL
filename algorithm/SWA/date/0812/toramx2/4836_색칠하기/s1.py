import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    red_box = []
    blue_box = []
    purple_box = []

    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))

        if color == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    red_box.append([i, j])

        elif color == 2:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    blue_box.append([i, j])

    for red in red_box:
        for blue in blue_box:
            if red == blue:
                purple_box.append(red)

    count = len(purple_box)

    print('#{0} {1}'.format(test_case, count))