import sys
sys.stdin = open('input.txt')
from itertools import combinations

N, M = map(int,input().split())
arr = list(map(int, input().split()))

# N개의 카드에서 3장을 뽑아
cards = list(combinations(arr, 3))
res = sum(cards[0])
# 그 합이 M이 안넘고 M에 가장 가까운 합이면 그것이 답
for set in cards:
    if abs(M-res) > abs(M-sum(set)) and sum(set) <= M:
        res = sum(set)

print(res)