import sys
sys.stdin = open('input.txt')



TC = 10
for tc in range(1, TC+1):
    # 덤프 횟수
    N = int(input())
    # 상자들의 높이
    boxes = list(map(int, input().split()))

