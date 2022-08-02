import sys
sys.stdin = open("input.txt")

N = int(input())
mine = sorted(list(map(int, input().split())))
M = int(input())
get = map(int, input().split())
res = {}


def binary(s, e, num, cnt):
    if s > e:
        return 0
    m = (s + e) // 2
    if mine[m] == num:
        return mine[s:e+1].count(num)
    elif mine[m] < num:
        return binary(m + 1, N, num, cnt)
    elif mine[m] > num:
        return binary(s, m - 1, num, cnt)

res = {}
for m in mine:
    s, e = 0, N
    if m not in res:
        res[m] = binary(s, e, m, 0)

for x in get:
    if x in res:
        print(res[x], end = ' ')
    else:
        print(0, end = ' ')
