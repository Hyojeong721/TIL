import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    lst = [[] for _ in range(E + 2)]
    for i in range(len(temp) // 2):
        lst[temp[2 * i]].append(temp[2 * i + 1])
    stack = lst[N][:]
    cnt = len(stack) + 1
    visited = [0] * (E + 2)
    while stack:
        a = stack.pop(0)
        visited[a] = 1
        for j in lst[a]:
            if not visited[j]:
                stack.append(j)
                cnt += 1
    print('#{} {}'.format(tc,cnt))



