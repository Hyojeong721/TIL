import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    print('#{}'.format(tc), end = ' ')

    N = int(input())
    numbers = list(map(int, input().split()))

    queue = []
    for n in numbers:
        queue.append(n)


    d = [1, 2, 3, 4, 5]
    i = 0

    v = queue.pop(0)
    while v >= 0:
        v = v-d[i]
        if v <= 0:
            queue.append(0)
            break
        else:
            queue.append(v)
        i = (i+1) % 5
        v = queue.pop(0)

    result = ''
    for i in queue:
        result += str(i) + ' '
    print(result)
