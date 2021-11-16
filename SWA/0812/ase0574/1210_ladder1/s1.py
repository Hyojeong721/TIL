# 0829
import sys
sys.stdin = open('input.txt')

def search_start(now_x, now_y):

    while now_x > 0:
        # 첫 본자리는 봣으니까 밑에 조건에 안걸리는 수로 바꾸기
        data[now_x][now_y] = 0

        # 왼쪽 오른쪽 살피기
        if 0 <= now_y-1 <= 99 and data[now_x][now_y-1] == 1:
            now_y -= 1

        # 오른쪽 살피기
        elif now_y+1 <= 99 and data[now_x][now_y+1] == 1:
            now_y += 1

        else:
            now_x -= 1

    return now_y

T = 10
for tc in range(1, T+1):
    # 테스트 케이스 번호
    N = int(input())
    # 100 x 100 크기의 2차원 배열로 주어진 사다리
    data = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0 for _ in range(100)] for _ in range(100)]

    # 도착점 좌표 찾기
    for i in range(100):
        if data[99][i] == 2:
            end = i

    print("#{} {}".format(tc, search_start(99, end)))
