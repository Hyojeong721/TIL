import sys
sys.stdin = open('input.txt')

T = 10

def dif(try_num, boxes):
    i = len(boxes)
    while i > 0:
        for j in range(i-1):
            if boxes[j] > boxes[j+1]:
                boxes[j+1], boxes[j] = boxes[j], boxes[j+1]
        i -= 1

    for _ in range(try_num):
        boxes[-1] -= 1
        if boxes[-1] < boxes[-2]:
            for i in range(len(boxes)-1):
                if boxes[-i-1] < boxes[-i-2]:
                    boxes[-i-1], boxes[-i-2] = boxes[-i-2], boxes[-i-1]
        boxes[0] += 1
        if boxes[0] > boxes[1]:
            for i in range(len(boxes)-1):
                if boxes[i] > boxes[i+1]:
                    boxes[i], boxes[i+1] = boxes[i+1], boxes[i]
    return boxes[-1] - boxes[0]

for tc in range(1, T+1):
    try_num = int(input())
    boxes = list(map(int, input().split()))
    print('#{} {}'.format(tc, dif(try_num, boxes)))