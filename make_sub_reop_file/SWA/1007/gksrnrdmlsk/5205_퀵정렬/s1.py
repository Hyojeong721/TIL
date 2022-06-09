import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    print('#{} {}'.format(tc, lst[N//2]))