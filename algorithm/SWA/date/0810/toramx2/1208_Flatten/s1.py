import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    count = 0

    while count < N:
        top = 0
        bottom = 100

        for box in boxes: #여기서 idx와 값을 한번에 하면?
            if box > top:
                top = box
            if box < bottom:
                bottom = box

        for idx, box in enumerate(boxes):
            if box == top:
                boxes[idx] = top - 1
                break;
        for idx, box in enumerate(boxes):
            if box == bottom:
                boxes[idx] = bottom + 1
                break;
        count += 1

    print('#{0} {1}'.format(test_case, max(boxes) - min(boxes)))