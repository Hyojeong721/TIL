import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    sorted_lst = []
    for idx, value in enumerate(lst):
        temp_value = lst[0]
        temp_idx = 0
        if value < temp:
            temp = value

