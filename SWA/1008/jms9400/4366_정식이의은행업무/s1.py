import sys
sys.stdin = open('input.txt')

T = int(input())


def change():  # 2진수를 1자리 바꾸고 10진수로 만들어주는 함수
    n = len(N)
    tmp = 0
    for i in N:
        tmp = tmp * 2 + int(i)

    for i in range(n):
        cand.append(tmp ^ (1 << i))

    for i in range(len(M)):
        num1 = 0
        num2 = 0
        for j in range(len(M)):
            if i != j:
                num1 = num1 * 3 + int(M[j])
                num2 = num2 * 3 + int(M[j])
            else:
                num1 = num1 * 3 + (int(M[j]) + 1) % 3
                num2 = num2 * 3 + (int(M[j]) + 2) % 3

        if num1 in cand:
            return num1
        if num2 in cand:
            return num2

for tc in range(1, T+1):
    N = input()
    M = input()
    cand = []

    print('#{} {}'.format(tc, change()))

