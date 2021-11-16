import sys
sys.stdin = open('input.txt')

def search(curr, past):
    global answer
    if past >= answer:
        return
    else:
        if lst[curr] == 0:
            if past < answer:
                answer = past
        else:
            for i in range(lst[curr], 0, -1):
                search(curr + i, past + 1)

T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input(). split()))
    N = lst[0]
    lst = lst[1:] + [0 for _ in range(N)]
    answer = N
    search(0, 0)
    print('#{} {}'.format(tc, answer - 1))
