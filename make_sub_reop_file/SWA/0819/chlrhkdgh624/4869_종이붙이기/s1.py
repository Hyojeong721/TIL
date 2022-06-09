import sys
sys.stdin = open('input.txt')

T = int(input())


def paper(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        # return paper(N-1) + 2*paper(N-2)
        return 2*paper(N-1) - paper(N-2)


for tc in range(1, T+1):
    N = int(input())/10
    result = paper(N)
    print(f'#{tc} {result}')