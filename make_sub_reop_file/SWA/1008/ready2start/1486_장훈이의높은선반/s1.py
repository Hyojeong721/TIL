import sys
sys.stdin = open('input.txt')


def get_min_height(i, height):
    """
    선반의 높이보다 크거나 같은 탑의 최소 높이를 구한다. (min_height에 저장)
    Args:
        i: 현재까지 탐색한 점원의 수
        height: 현재까지의 탑의 높이
    """
    global N, B, heights, min_height

    # 현재 탑의 높이가 B 이상인 경우 => min_height와 비교한 뒤, 탐색 종료
    if height >= B:
        min_height = min(min_height, height)
        return

    # 모든 점원을 다 탐색한 경우 => 탐색 종료
    # 높이가 B 이상인 경우는 위 if문에서 검사했으므로, 바로 return함.
    if i == N:
        return

    # i번째 점원을 탑에 포함하지 않는 경우
    get_min_height(i + 1, height)
    # i번째 점원을 탑에 포함하는 경우
    get_min_height(i + 1, height + heights[i])


T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    heights = [int(x) for x in input().split()]
    min_height = 1000000

    get_min_height(0, 0)
    print("#{} {}".format(t, min_height - B))
