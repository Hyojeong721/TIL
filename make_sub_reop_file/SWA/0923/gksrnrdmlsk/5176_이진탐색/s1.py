import sys
sys.stdin = open('input.txt')

# 이진트리: 왼쪽 자식 - 부모 - 오른쪽 자식 순서 탐색
def bin_tree(curr):
    global visited, temp, lst
    if curr * 2 <= N:
        bin_tree(curr * 2)

    visited[curr] = 1
    lst[curr] = temp.pop(0)

    if curr * 2 + 1 <= N:
        bin_tree(curr * 2 + 1)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * (N + 1)
    temp = list(range(1, N + 1))
    lst = [0] * (N + 1)
    bin_tree(1)
    print('#{} {} {}'.format(tc, lst[1], lst[N // 2]))

