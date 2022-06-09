import sys
sys.stdin = open('input.txt')

T = int(input())

def Swap(N, n, i, M):
    if i == M:
        a = int(''.join(N[:]))
        num_lst.append(a)
    else:
        a = list(N)
        if a in visited:
            return
        visited.append(a)
        for x in range(n):
            for y in range(x+1, n):
                # if (i > 1 and N[0] != max(N)) or (i > 2 and N[1] != max(N[1:])) or (i > 3 and N[2] != max(N[2:])):
                #     break
                # else:
                    N[x], N[y] = N[y], N[x]
                    Swap(N, n, i+1, M)
                    N[x], N[y] = N[y], N[x]

for tc in range(1, T+1):
    N, M = input().split()
    M = int(M)
    N = list(N)
    n = len(N)
    num_lst = []
    visited = []
    Swap(N, n, 0, M)
    print(f'{tc} {max(num_lst)}')
