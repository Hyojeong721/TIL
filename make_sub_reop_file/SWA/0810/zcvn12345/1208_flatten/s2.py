import sys
sys.stdin = open('input.txt')
# 상자의 높이는 1이상 100이하
# 가로 길이는 항상 100
# min, max 초기화!!

T = 10
# 조망권이 확보된 세대의 수
answer = 0
flatten = False
for test_case in range(1, T+1):
    dump_cnt = int(input())
    box_height = list(map(int, input().split()))
    while dump_cnt != 0 and flatten != True:
        max_height = 1
        min_height = 100
        max_idx = min_idx = 0
        for i in range(1, 100):
            for idx, num in enumerate(box_height):
                if num >= max_height:
                    max_height = num
                    max_idx = idx
                if num <= min_height:
                    min_height = num
                    min_idx = idx
        box_height[max_idx] -= 1
        box_height[min_idx] += 1
        if box_height[max_idx] - box_height[min_idx] == 1:
            flatten = True
        dump_cnt -= 1
        answer = box_height[max_idx] - box_height[min_idx] + 2
    print('#{} {} '.format(test_case, answer))