# 동적계획법 풀이

import sys
sys.stdin = open("input.txt")


def count_set(width):
    """
    (20 X l) 크기의 교실 바닥이 주어졌을 때
    (10 X 20) 타일과 (20 X 20) 타일로
    교실 바닥을 모두 채우는 경우의 수를 구한다.

    Args:
        width: 교실 바닥의 가로 길이
    Returns:
        타일로 교실 바닥을 채우는 경우의 수
    """
    # 가로 길이가 10인 경우
    if width == 10:
        # (10 X 20) 1개
        return 1

    # 가로 길이가 20인 경우
    if width == 20:
        # (10 X 20) 2개 / (20 X 10) 2개 / (20 X 20) 1개
        return 3

    # counts[n] : 가로 길이가 10n일 때 바닥을 채우는 경우의 수
    counts = [0, 1, 3]

    """
    가로 길이가 30 이상인 경우
        a. 맨 왼쪽이 (10 X 20) 1개인 경우 = count_set(width - 10)
        b. 맨 왼쪽이 (20 X 10) 2개인 경우 = count_set(width - 20)
        c. 맨 왼쪽이 (20 X 20) 1개인 경우 = count_set(width - 20)
    """
    for i in range(3, width // 10 + 1):
        cnt = counts[i - 1] + 2 * counts[i - 2]
        counts.append(cnt)

    return counts[-1]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    print("#{} {}".format(tc, count_set(N)))
