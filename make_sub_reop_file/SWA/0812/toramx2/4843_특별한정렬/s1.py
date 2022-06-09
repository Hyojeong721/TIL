import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    special = []

    for i in range(0, N - 1):
        max = i
        for j in range(i+1, N):
            if ai[max] < ai[j]:
                max = j
        ai[i], ai[max] = ai[max], ai[i]

    for i in range(N // 2, N - 1):
        min = i
        for j in range(i+1, N):
            if ai[min] > ai[j]:
                min = j
        ai[i], ai[min] = ai[min], ai[i]

    for i in range(0, N //2):
        special.append(ai[i])
        special.append(ai[i + N//2])

    print('#{0}'.format(test_case), end = ' ')
    for num in range(10):
        print(special[num], end = ' ')
    print()
