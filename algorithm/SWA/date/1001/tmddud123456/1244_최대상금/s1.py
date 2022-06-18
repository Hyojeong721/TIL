import sys
sys.stdin = open('input.txt')

def changeMoney(N, M):
    global total, change

    if (change-M)%2 == 0:
        if total[-1] > int(''.join(N)):
            return 0
    if M == change:
        total.append(int(''.join(N)))
        return 0

    for i in range(len(N)):
        for j in range(i+1, len(N)):
            N[i], N[j] = N[j], N[i]
            changeMoney(N, M+1)
            N[i], N[j] = N[j], N[i]

TC = int(input())

for tc in range(1, TC + 1):
    quiz, change = list(map(int, input().split()))
    quiz = list(str(quiz))
    total = []
    total.append(0)
    changeMoney(quiz, 0)
    # print(total)
    print('#{} {}'.format(tc, total[-1]))