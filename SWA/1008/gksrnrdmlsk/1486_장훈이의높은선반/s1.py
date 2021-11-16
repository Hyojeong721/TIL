import sys
sys.stdin = open('input.txt')

def search(curr, cnt):
    global answer
    if cnt - B > answer:
        return
    if curr == N:
        if 0 <= cnt - B < answer:
            answer = cnt - B
        return
    search(curr + 1, cnt)
    search(curr + 1, cnt + lst[curr])

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    answer = 1000000
    search(0, 0)
    print('#{} {}'.format(tc, answer))