import sys
sys.stdin = open('input.txt')

def harvest(area):
    total = 0
    center = len(area) // 2

    total += area[center][center]

    j = 1
    while j < center + 1:
        for i in range(j):
            total += area[center-i][center-j+i]     # 좌부터 대각선 우로            열이 좌측으로 j만큼씩 가면서 그때마다 대각선 위로 한칸씩
            total += area[center-j+i][center+i]     # 상부터 대각선 아래로
            total += area[center+i][center+j-i]     # 우부터 대각선 아래로
            total += area[center+j-i][center-i]     # 하부터 대각선 좌로
        j += 1

    return total


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input())) for _ in range(N)]
    print('#{} {}'.format(test_case, harvest(area)))