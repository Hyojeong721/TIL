import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    n_dumps = int(input())
    heights = list(map(int, input().split()))

    for d in range(n_dumps):
        max_height = 0
        min_height = 101

        for i in range(100):
            if max_height < heights[i]:
                max_height = heights[i]
                max_idx = i
            if min_height > heights[i]:
                min_height = heights[i]
                min_idx = i
        heights[max_idx] -= 1
        heights[min_idx] += 1

        max_height2 = 0
        min_height2 = 101
        for j in range(100):
            if max_height2 < heights[j]:
                max_height2 = heights[j]
            if min_height2 > heights[j]:
                min_height2 = heights[j]

    result = max_height2 - min_height2

    print('#{} {}'.format(t, result))

