import sys
sys.stdin = open('input.txt')

T = int(input())


def Bbit_print(i):
    output = ""
    for j in range(3, -1, -1):
        output += "1" if i & (1<<j) else "0"
    return output


for tc in range(1, T + 1):
    N, number = input().split()
    answer = ''

    for i in range(int(N)):
        answer += Bbit_print(int(number[i], 16))
    print('#{} {}'.format(tc, answer))