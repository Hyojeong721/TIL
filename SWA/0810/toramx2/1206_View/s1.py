import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    segment_buildings = []
    prospect = []

    for i in range(N - 4):
        segment_buildings.append(buildings[i:i + 5])

    for segment in segment_buildings:
        if max(segment) == segment[2]:
            prospect.append(segment[2] - sorted(segment)[3])

    print('#{0} {1}'.format(test_case, sum(prospect)))