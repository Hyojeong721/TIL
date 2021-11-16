import sys
sys.stdin = open('input.txt')

def inorderT(T):
    result = []
    if T:
        inorderT(left[T])
        print(words[T], end='')
        inorderT(right[T])

T = 10
for tc in range(1, T+1):
    V = int(input())

    left = [0] * (V+1)
    right = [0] * (V+1)

    words = [0] * (V+1)

    for i in range(V):
        info = list(input().split())

        if len(info) == 2:
            p = int(info[0])
            words[p] = info[1]

        elif len(info) == 3:
            p = int(info[0])
            words[p] = info[1]
            c = int(info[2])
            left[p] = c

        elif len(info) == 4:
            p = int(info[0])
            words[p] = info[1]
            c1 = int(info[2])
            c2 = int(info[3])
            if c1 > c2:
                left[p] = c2
                right[p] = c1
            else:
                left[p] = c1
                right[p] = c2

    print('#{}'.format(tc), end=' ')
    inorderT(1)
    print()








