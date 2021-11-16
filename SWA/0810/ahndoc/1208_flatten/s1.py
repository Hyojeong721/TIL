import sys
sys.stdin = open("input.txt", "r")

TC = 10
for tc in range(1, TC + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for i in range(dump):
        max_box = boxes[0]
        for box in boxes:
            if box > max_box:
                max_box = box

        min_box = boxes[0]
        for box in boxes:
            if box < min_box:
                min_box = box

        boxes[boxes.index(max_box)] -= 1
        boxes[boxes.index(min_box)] += 1

    max_box = boxes[0]
    for box in boxes:
        if box > max_box:
            max_box = box

    min_box = boxes[0]
    for box in boxes:
        if box < min_box:
            min_box = box

    result = max_box - min_box

    print('#{} {}'.format(tc, result))







