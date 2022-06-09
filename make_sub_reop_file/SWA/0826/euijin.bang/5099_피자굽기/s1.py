import sys
sys.stdin = open("input.txt")

# 피자굽기 - c

# N => 화덕의 크기, M => 피자의 개수

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split())) # 3 5
    # [7, 2, 6, 5, 3]
    q = []
