import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    for string in arr:
        for i in range(N-M+1):
            str_tmp = []
            for j in range(M):
                str_tmp.append(string[i+j])

        if str_tmp == list(reversed(str_tmp)):
            print('#{} {}'.format(tc, ''.join(str_tmp)))

    for i in range(N):
        str_tmp = []
        for j in range(len(arr[i])-M+1):
            for k in range(M):
                str_tmp.append(arr[j+k][i])

        if str_tmp == list(reversed(str_tmp)):
            print('#{} {}'.format(tc, ''.join(str_tmp)))
