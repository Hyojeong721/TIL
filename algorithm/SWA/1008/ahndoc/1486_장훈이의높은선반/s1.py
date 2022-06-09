import sys
sys.stdin = open('input.txt')
from itertools import permutations

"""
부분집합
"""
def find(idx, s, rs):
    global ans

    if s >= B:
        if ans > s - B:
            ans = s - B
        return

    if idx == N:
        return

    find(idx + 1, s + heights[idx], rs - heights[idx])
    find(idx + 1, s, rs - heights[idx])

# def find2(s):
#     global ans
#     if ans <= s-B:
#         return
#
#     if s >= B:
#         ans = s-B
#         return
#
#     else:
#         for i in range(N):
#             if not used[i]:
#                 used[i] = 1
#                 find(s + heights[i])
#                 used[i] = 0



T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort()
    used = [0] * N
    ans = 987654321
    find(0, 0, sum(heights))
    print('#{} {}'.format(tc, ans))