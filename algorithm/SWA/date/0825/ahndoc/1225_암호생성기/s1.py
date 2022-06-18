import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    tc = int(input())
    arr = list(map(int, input().split()))

    while True:
        for n in range(1, 6):
            v = arr.pop(0) - n

            if v <= 0:
                v = 0
                arr.append(v)
                break

            else:
                arr.append(v)

        if arr[7] == 0:
            break

    print('#{}'.format(tc), end = ' ')
    print(*arr)



