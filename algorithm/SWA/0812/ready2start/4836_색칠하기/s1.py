import sys
sys.stdin = open("input.txt")


def paint_color(area, points):
    """2차원 배열에서 주어진 좌표에 해당하는 영역을 칠한다. (칠한 부분은 True 표시)

    area: 색을 칠해야 하는 바탕 영역 (2차원 배열)
    points: [r1, c1, r2, c2]로 이루어진 배열
        - (r1, c1) : 칠해야 하는 부분의 왼쪽 위 모서리 인덱스
        - (r2, c2) : 칠해야 하는 부분의 오른쪽 아래 모서리 인덱스
    """
    r1, c1, r2, c2 = points

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            area[r][c] = True


T = int(input())

for tc in range(1, T + 1):
    """
    red_area: 빨간색을 칠할 부분을 표시하는 배열
    blue_area: 파란색을 칠할 부분을 표시하는 배열
    """
    red_area = [[False] * 10 for _ in range(10)]
    blue_area = [[False] * 10 for _ in range(10)]

    N = int(input())
    for _ in range(N):
        *points, color = list(map(int, input().split()))

        if color == 1:
            paint_color(red_area, points)
        else:
            paint_color(blue_area, points)

    # purple_area = 빨간색과 파란색이 모두 칠해진 인덱스의 개수
    purple_area = 0

    for r in range(10):
        for c in range(10):
            if red_area[r][c] and blue_area[r][c]:
                purple_area += 1

    print("#{} {}".format(tc, purple_area))
