import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    # dump 횟수만큼 for문 사용
    for i in range(dump):
        max_value = boxes[0]
        min_value = boxes[0]
        max_number = 0
        min_number = 0
        # 가장 높은 곳에서 -1, 가장 낮은 곳에서 +1
        for j in range(len(boxes)):
            # 가장 높은 곳 찾는 코드
            if max_value < boxes[j]:
                max_value = boxes[j]
                max_number = j
            # 가장 낮은 곳 찾는 코드
            if min_value > boxes[j]:
                min_value = boxes[j]
                min_number = j
        boxes[max_number] -= 1
        boxes[min_number] += 1

    # 덤프 작업이 모두 끝난 후 가장 높은 층과 가장 낮은 층의 차를 구함
    max_value_after_dump = boxes[0]
    min_value_after_dump = boxes[0]

    for i in range(1, len(boxes)):
        if max_value_after_dump < boxes[i]:
            max_value_after_dump = boxes[i]
        if min_value_after_dump > boxes[i]:
            min_value_after_dump = boxes[i]
    result = max_value_after_dump - min_value_after_dump

    print('#{0} {1}'.format(test_case, result))
