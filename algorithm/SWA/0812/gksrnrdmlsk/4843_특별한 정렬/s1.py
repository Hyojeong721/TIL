import sys
sys.stdin = open('input.txt')

T = int(input())

# def special_sort(list):
#     if len(list) == 2:
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    temp_idx = 0

    for idx in range(N):
        temp_value = lst[idx]
        if not idx % 2:
            for i, j in enumerate(lst[idx:]):
                if j > temp_value:
                    temp_value = j
                    max_idx = i
            lst[idx], lst[temp_idx] = lst[temp_idx], lst[idx]

        else:
            for i, j in enumerate(lst[idx:]):
                if j < temp_value:
                    temp_value = j
                    temp_idx = i
            lst[idx], lst[temp_idx] = lst[temp_idx], lst[idx]

    print(lst)
