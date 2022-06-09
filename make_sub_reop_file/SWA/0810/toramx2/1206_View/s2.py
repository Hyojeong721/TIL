# 잘못된 풀이
import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    segment_buildings = []
    prospect = []

    for i in range(2, len(buildings)-3):
        segment_buildings = buildings[i-2:i+3]
        if segment_buildings[2] == max(segment_buildings):
            prospect.append(max(segment_buildings) - sorted(segment_buildings)[3])

    print('#{0} {1}'.format(test_case, sum(prospect)))

    # for test_case in range(1, 11):
    #     N = int(input())
    #     buildings = list(map(int, input().split()))
    #     segment_buildings = []
    #     prospect = []
    #
    #     for i in range(N - 4):
    #         segment_buildings.append(buildings[i:i + 5])
    #
    #     for segment in segment_buildings:
    #         if max(segment) == segment[2]:
    #             prospect.append(segment[2] - sorted(segment)[3])
    #
    #     print('#{0} {1}'.format(test_case, sum(prospect)))