import sys
sys.stdin = open('input.txt')


"""
[탐색 규칙]
1. 맨 위에 놓인 상자만 확인하면 된다.
   (높이가 더 낮은데 오른쪽에 상자가 더 적을 수는 없고, 이는 낙차가 더 클 수는 없음을 의미한다.)
2. 맨 위에 놓인 상자의 낙차
   = 가로 끝에서 현재 위치의 거리 - 사이에 있는 상자의 수
   = 오른쪽에 자신보다 높이가 낮은 상자 더미의 수
3. 왼쪽에 더 높은 상자가 있는 경우는 확인할 필요가 없다.
   (그 상자보다 오른쪽에 자기보다 높이가 낮은 상자 더미의 수가 더 적으므로)
"""


def get_max_falling(heights):
    """
    상자를 오른쪽으로 90도 회전했을 때 낙차가 가장 큰 상자의 낙차를 구한다.
    heights: 상자의 높이 배열

    max_height : 현재까지 탐색한 상자 더미의 최대 높이
    max_falling : 최대 낙차
    falling: 현재 탐색 중인 상자의 낙차
    """
    max_height = 0
    max_falling = 0

    for i in range(len(heights)):
        # 왼쪽에 더 높은 상자 더미가 없다면
        if max_height <= heights[i]:
            max_height = heights[i]
            falling = 0

            for j in range(i + 1, len(heights)):
                # 낙차 = 오른쪽에 자신보다 높이가 낮은 상자 더미의 수
                if heights[j] < heights[i]:
                    falling += 1

            if falling > max_falling:
                max_falling = falling

    return max_falling


M = int(input())

for _ in range(M):
    N = int(input())
    heights = list(map(int, input().split()))

    max_falling = get_max_falling(heights)
    print(max_falling)
