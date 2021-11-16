import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):
    answer = 0
    num = int(input())
    box = list(map(int, input().split()))

    for i in range(len(box)):
        for j in range(0, len(box) - i - 1):
            if box[j] > box[j + 1]:
                box[j], box[j + 1] = box[j + 1], box[j]

    min_height = box[0]
    max_height = box[len(box) - 1]
    min_before = box[0]
    max_before = box[len(box) - 1]
    max_num = 1
    move = 0



    for i in range(1, len(box)):
        if box[i - 1] == box[i]:
            continue
        cnt = (box[i] - box[i - 1]) * i

        if move + cnt <= num:
            move += cnt
            min_height = box[i]
        else:
            min_height += (num - move) // (i - 1)
            break

    for j in range(1, len(box)):
        if box[len(box) - j] == box[len(box) - j - 1]:
            continue

        cnt2 = (box[len(box) - j] - box[len(box) - j - 1]) * j
        if move - cnt2 >= 0:
            move -= cnt2
            max_height = box[len(box) - j - 1]
        else:
            max_height -= move // (len(box) - j)
            break

    print(min_height)
    print(max_height)
    print('-----------------')
    answer = max_height - min_height

    if max_height == min_height:
        if move % 100 == 0:
            answer = 0
        else:
            answer = 1

