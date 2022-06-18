# swea 1206 View
# 조망권 확보된 세대 수 출력
import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    len_b = int(input())
    # 각 케이스의 첫 줄에 주어진 양수의 개수를 받아, 빌딩 리스트로 만든다.
    buildings = list(map(int, input().split()))
    cnt = 0
    # 예시의 빨간 땅 부분을 2만큼씩 빼야한다.
    for i in range(2, len_b-2):
        # 좌우로 2개보다 큰 경우들을 생각한다.
        if buildings[i] > buildings[i-1] \
                and buildings[i] > buildings[i-2] \
                and buildings[i] > buildings[i+1] \
                and buildings[i] > buildings[i+2]:
            # 값 차이가 가장 적을 때 높이가 가장 높다.
            d1 = buildings[i] - buildings[i-2]
            d2 = buildings[i] - buildings[i-1]
            d3 = buildings[i] - buildings[i+1]
            d4 = buildings[i] - buildings[i+2]
            min_diff = d1
            for diff in [d1, d2, d3, d4]:
                if diff < min_diff:
                    min_diff = diff
            cnt += min_diff
    print('#{} {}'.format(tc, cnt))

