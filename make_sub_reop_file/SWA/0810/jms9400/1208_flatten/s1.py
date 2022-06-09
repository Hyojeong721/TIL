import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()

    for i in range(n):
        boxes[-1] -= 1
        boxes[0] += 1
        boxes.sort()

    max_box = boxes[-1]
    min_box = boxes[0]

    print('#{} {}'.format(tc, max_box - min_box))