import sys
from itertools import permutations
sys.stdin = open('input.txt')

T = int(input())


def find_road(a, s, idx):
    if idx >= len(a):
        s_lst.append(s+arr[a[idx-1]][0])
        return
    if s == 0:
        find_road(a, arr[0][a[idx]], idx+1)
    else:
        find_road(a, s + arr[a[idx-1]][a[idx]], idx+1)


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [i for i in range(1, N)]
    perm = list(permutations(lst, N-1))
    s_lst = []

    for p in perm:
        find_road(p, 0, 0)
    print('#{} {}'.format(tc, min(s_lst)))
