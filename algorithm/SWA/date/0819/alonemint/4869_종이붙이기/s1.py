import sys
sys.stdin = open('input.txt')

T = int(input())

def paper_recursive(n):
    if n <= 2:
        return 2 * n - 1
    else:
        return paper_recursive(n - 1) + 2 * paper_recursive(n - 2)

for tc in range(1, T + 1):

    N = int(input())
    res = paper_recursive(N // 10)
    print('#{} {}'.format(tc, res))