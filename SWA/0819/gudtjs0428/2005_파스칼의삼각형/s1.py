import sys
sys.stdin = open('input.txt')

def pascal_tri(N):
    tri = [[] for _ in range(N+1)]
    tri[1].append(1)
    if N >= 2:
        tri[2].append(1)
        tri[2].append(1)

    for i in range(3, N+1):
        for n in range(i):
            if n == 0 or n == i-1:
                tri[i].append(1)
            else:
                tri[i].append(tri[i-1][n-1] + tri[i-1][n])

    return tri


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(1, N+1):
        for n in pascal_tri(N)[i]:
            print(n, end=' ')
        print()