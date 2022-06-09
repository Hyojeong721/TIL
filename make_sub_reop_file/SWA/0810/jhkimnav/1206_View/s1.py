import sys
sys.stdin = open('input.txt')

T = 10
# 조망권이 확보된 세대의 수
for test_case in range(1, T+1):
    answer = 0
    # N 빌딩 갯수, 가로 길이
    N = int(input())
    building_height = list(map(int, input().split()))
    for i in range(2, N-2):
        # i번째 빌딩의 좌우로 2만큼 인접 빌딩 중 최대 높이 찾기
        temp = 0
        max_height = 0
        for j in range(1, 3):
            if max_height < building_height[i-j]:
                max_height = building_height[i-j]
        for k in range(1, 3):
            if max_height < building_height[i+k]:
                max_height = building_height[i+k]

        # i번째 건물의 높이가 좌우 인접 빌딩의 최대 높이보다 높다면
        # 해당 차이만큼 조망권 확보된 세대의 수 count
        if building_height[i] - max_height > 0:
            answer += building_height[i] - max_height
    print('#{} {} '.format(test_case, answer))
