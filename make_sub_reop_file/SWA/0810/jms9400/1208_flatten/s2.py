import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    boxes = list(map(int, input().split()))

    for i in range(n):
        max_box = max(boxes)
        idx = boxes.index(max_box)
        boxes[idx] -= 1
        min_box = min(boxes)
        idx2 = boxes.index(min_box)
        boxes[idx2] += 1

    max_box = max(boxes)
    min_box = min(boxes)

    print('#{} {}'.format(tc, max_box - min_box))