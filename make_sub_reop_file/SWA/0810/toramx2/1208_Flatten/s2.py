# 잘못된 풀이

import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    count = 0

    while count < N:
        top = 0
        bottom = 100

        for box in boxes:
            if box > top:
                top = box
            if box < bottom:
                bottom = box

        # 리스트의 값을 바꾸기 위해선 index 접근을 해야한다
        # 아래와 같은 방법으로는 바뀌지 않음
        for box in boxes:
            if box == top:
                box = top - 1
                break;
        for box in boxes:
            if box == bottom:
                box = bottom + 1
                break;
        count += 1

    print('#{0} {1}'.format(test_case, max(boxes) - min(boxes)))