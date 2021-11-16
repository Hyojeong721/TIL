import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = 5
    lst = [list(input()) for _ in range(N)]
    maxi = max(map(len, lst))
    for i in lst:
        if len(i) < maxi:
            i += ['!'] * (maxi - len(i))
    print('#%s' %tc, end=' ')
    for c in range(maxi):
        for r in range(N):
            if lst[r][c] != '!':
                print(lst[r][c], end='')

    print()