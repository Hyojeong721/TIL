import sys
sys.stdin = open('input.txt')

T = int(input())


def Bbit_print(i):
    output = ""
    for j in range(N, -1, -1):
        output += "1" if i & (1<<j) else "0"
    return output

for tc in range(1, T + 1):
    N, M = input().split()
    N = int(N)

    answer = Bbit_print(int(M))

    if answer[-N:] == '1' * N:
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))