import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))

    # 한 숫자가 0에 도달할 때까지 cycle 돌림
    cnt = -1
    while True:
        cnt = (cnt + 1) % 5     # 0 1 2 3 4
        deQ = data.pop(0)
        deQ -= cnt + 1

        if deQ > 0:
            data.append(deQ)
        else:
            data.append(0)
            break

    # 문자열로 합친 후 출력
    result = ''
    for n in data:
        result += '{} '.format(str(n))
    print('#{} {}'.format(tc, result))
