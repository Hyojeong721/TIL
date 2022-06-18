import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    A = input()
    A = A.replace('()','L')
    F = 0
    total = 0

    for i in A:
        if i == '(':
            F += 1

        elif i ==')':
            total += 1
            F -= 1

        elif i =='L':
            total += F

    print('#{} {}'.format(tc, total))