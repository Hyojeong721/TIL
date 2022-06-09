import sys
sys.stdin = open('input.txt')
# X번 집으로 오고 가는데 드는 시간 중에서 가장 오래 걸리는 집은 어느 정도 걸리는지 구하는 프로그램을 작성하라.

def go_to_X(start, time):





T = int(input())
for tc in range(1):
    # 1~ N번까지 집 / M개의 정보 / X번집
    N, M, X = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    visited = [0] * N

    ans = 0
    get

    print(go_time)