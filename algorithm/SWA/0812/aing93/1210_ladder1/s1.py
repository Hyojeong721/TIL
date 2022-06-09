import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 값이 2인 목표지점 찾기
    target = 0
    for i in range(100):
        if ladder[99][i] == 2:
            target = i
            break

    x = target
