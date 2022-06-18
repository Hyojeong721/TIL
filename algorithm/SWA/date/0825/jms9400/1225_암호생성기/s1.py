import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, (input().split())))
    lst = [1, 2, 3, 4, 5]

    while len(arr):
        a = arr.pop(0)
        b = lst.pop(0)
        c = a - b
        if c <= 0:
            c = 0
            arr.append(c)
            break
        arr.append(c)
        lst.append(b)

    print('#{} {}'.format(N, ' '.join(map(str, arr))))
