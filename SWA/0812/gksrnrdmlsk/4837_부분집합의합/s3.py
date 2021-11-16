# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# superset = list(range(1, 13))
#
# def sub_gen(list, n):
#     for i in range(len(list)):
#         for j in range(i, len(list)):
#
#
# for tc in range(1, T + 1):
#     N, K = list(map(int, input().split()))
#     N = int(input())
#     lst_red = [[0] * 10 for _ in range(10)]
#     lst_blue = [[0] * 10 for _ in range(10)]
#     cnt = 0
#     for n in range(N):
#         lst = list(map(int, input().split()))

k = 4
super_lst = []
lst = list(range(k))
for i in range(k-1, -1, -1):
        while lst[i] <= 11 - k + i:
            super_lst.append(lst[:])
            lst[i] = lst[i] + 1

print(super_lst)