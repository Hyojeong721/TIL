import sys
sys.stdin = open('input.txt')

T = int(input())


def pascal(n):
    if n == 1:
        return [1]
    else:
        padding = [0] + pascal(n-1) + [0]
        result = [0] * n
        for i in range(len(padding)-1):
            result[i] = padding[i] + padding[i+1]
        return result


for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(1, N+1):
        print(' '.join(map(str, pascal(i))), end='\n')