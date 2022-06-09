import sys
sys.stdin = open('input.txt')


def count_view_building(region, buildings):
    """
    해당 지역에 있는 건물들의 각 층 중에서 조망권을 확보한 세대의 수를 반환

    region: 지역의 가로 길이 (constant)
    buildings: 지역내의 건물들의 높이 (list)

    counts: 조망권을 확보한 세대 수
    """
    counts = 0

    # 첫 건물부터 마지막 건물 탐색
    for x in range(2, region - 2):
        # 수정 후
        # 주변 건물 중 가장 큰 건물의 높이
        max_surr = buildings[x - 2]
        if max_surr < buildings[x - 1]:
            max_surr = buildings[x - 1]
        if max_surr < buildings[x + 1]:
            max_surr = buildings[x + 1]
        if max_surr < buildings[x + 2]:
            max_surr = buildings[x + 2]

        diff = buildings[x] - max_surr
        if diff > 0:
            counts += diff

        # 수정 전
        # # 해당 건물의 꼭대기 층 높이부터 내려오며 조망권 검사
        # for y in range(buildings[x], 0, -1):
        #     # 현재 높이에서 조망권 확보되면, count 에 1 추가
        #     if buildings[x-2] < y and buildings[x-1] < y and buildings[x+1] < y and buildings[x+2] < y:
        #         counts += 1
        #     # 현재 높이에서 조망권 확보 안되면, 아래도 마찬가지므로 break
        #     else:
        #         break

    return counts


for tc in range(1, 11):
    region = int(input())
    buildings = list(map(int, input().split()))
    views = count_view_building(region, buildings)
    print('#{0} {1}'.format(tc, views))
