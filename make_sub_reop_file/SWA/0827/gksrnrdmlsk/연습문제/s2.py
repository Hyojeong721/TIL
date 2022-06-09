# 유튜브 교수님의 풀이
def pre_order(n):
    if n:
        print(n)
        pre_order(left[n])
        pre_order(right[n])

def in_order(n):
    if n:
        in_order(left[n])
        print(n)
        in_order(right[n])



import sys
sys.stdin = open('input.txt')


V = int(input())
lst = list(map(int, input().split()))
E = V - 1
left = [0] * (V + 1)
right = [0] * (V + 1)
for i in range(E):
    if not left[lst[2 * i]]:
        left[lst[2 * i]] = lst[2 * i + 1]
    else:
        right[lst[2 * i]] = lst[2 * i + 1]

in_order(1)
pre_order(1)