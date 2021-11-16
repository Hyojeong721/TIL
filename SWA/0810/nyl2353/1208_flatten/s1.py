import sys
sys.stdin = open('input.txt')


def flatten(dumps, heights):
    # 오름차순으로 정렬
    heights.sort()

    while dumps:
        # 수정
        # 가장 큰 값과 가장 작은 값의 차이가 0 또는 1이면 반복문 종료
        if heights[99] - heights[0] <= 1:
            break

        # 하나씩 옮기고, 정렬된 상태 유지
        heights[0] += 1
        heights[99] -= 1
        dumps -= 1
        heights.sort()

    diff = heights[99] - heights[0]
    return diff

for tc in range(1, 11):
    dumps = int(input())
    heights = list(map(int, input().split()))
    diff = flatten(dumps, heights)
    print('#{0} {1}'.format(tc, diff))


    # # 원래 while 문 내에서 시도 했던 것... 어차피 sort 쓸 걸 왜 이렇게 했는지?
    # # 가장 높은 높이의 상자들
    # for i in range(99, -1, -1):
    #     if heights[i] == heights[99]:
    #         margin_h = i
    #     else:
    #         break
    #
    # # 가장 낮은 높이의 상자들
    # for i in range(99):
    #     if heights[i] == heights[0]:
    #         margin_l = i
    #     else:
    #         break
    #
    # # 제일 높은 높이인 상자들의 개수만큼 진행
    # for i in range(100 - margin_h):
    #     heights[margin_h + i] -= 1
    #     heights[margin_l - i] += 1
    #     dumps -= 1
