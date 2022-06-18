
def subtree(n):
    global cnt
    if n:
        cnt += 1
        subtree(left[n])
        subtree(right[n])

    return cnt

# N : 서브 트리의 루트
import sys
sys.stdin = open('input.txt')

T = int(input())

for T in range(1, T+1):
    E, N = list(map(int, input().split()))
    edge = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    answer = subtree(N)
    print('#{} {}'.format(T, answer))

