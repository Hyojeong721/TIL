import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(T):
    N, T = map(int, input().split()) # N 지도 한 변의 길이, K 최대 공사 가능 깊이
    maps = [list(map(int, input().split())) for _ in range(N)]
    print(maps)
    # 이차원 리스트 델타 탐색 (상우하좌)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    max_maps = max(map(max, maps))
    min_maps = min(map(min, maps))
    roads_cnt = []

    for row in range(N):
        for col in range(N):
            # 가장 높은 봉우리 찾기
            if maps[row][col] == max_maps:
                gaps = []
                k = 0
                while k < 4:
                    new_row = row + dx[k]
                    new_col = col + dy[k]
                    # 1번 봉우리와의 차이가 가장 적은 방향으로 전진
                    if 0 <= new_row < N and 0 <= new_col < N:
                        gap = maps[row][col] - maps[new_row][new_col]
                        gaps.append(gap)
                    else:
                        gaps.append(99)
                    k += 1

                print(gaps)   #[6, 3, 99, 99]
                min_gap = min(gaps)

                # 차이가 가장 적은 방향으로 전진
                k = gaps.index(min_gap)
                row = row + dx[k]
                col = col + dy[k]
                cnt += 1
                roads_cnt.append(cnt)

    print("#{} {}".format(tc+1, max(roads_cnt)))


