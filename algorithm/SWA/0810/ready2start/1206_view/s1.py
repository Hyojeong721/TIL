import sys
sys.stdin = open('input.txt')

"""
세대 A가 조망권을 확보한다
= 양쪽 모두 거리 2 이상의 공간이 있다
= 양쪽 두 빌딩의 건물 높이가 세대 A 높이보다 낮다
"""


def get_highest_around(heights, idx):
    """
    idx번째 빌딩의 (왼쪽 빌딩 2개 + 오른쪽 빌딩 2개)의 최고 높이를 구한다.
    max_height: 빌딩 4개 중 가장 높은 빌딩의 높이

    max(heights[idx - 2], heights[idx - 1], heights[idx + 1], heights[idx + 2])와 같은 값을 반환한다.
    """
    max_height = heights[idx - 2]

    if heights[idx - 1] > max_height:
        max_height = heights[idx - 1]
    if heights[idx + 1] > max_height:
        max_height = heights[idx + 1]
    if heights[idx + 2] > max_height:
        max_height = heights[idx + 2]

    return max_height


def count_view(width, heights):
    """
    조망권이 확보된 세대의 수를 구한다.
    width: 가로 길이
    heights: 빌딩들의 높이 (list)

    total: 조망권이 확보된 세대의 총합
    highest_around: (왼쪽 빌딩 2개 + 오른쪽 빌딩 2개)의 최고 높이
    """
    total = 0

    # 왼쪽 2칸, 오른쪽 2칸은 제외하고 탐색 진행
    for i, height in enumerate(heights[2:-2:], 2):
        highest_around = get_highest_around(heights, i)
        if height > highest_around:
            total += (height - highest_around)

    return total


for tc in range(1, 11):
    width = int(input())
    heights = list(map(int, input().split()))

    # views: heights 배열에서 조망권이 있는 빌딩의 수
    views = count_view(width, heights)
    print("#{} {}".format(tc, views))
