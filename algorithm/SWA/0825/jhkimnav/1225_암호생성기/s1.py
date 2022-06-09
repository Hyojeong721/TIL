import sys
sys.stdin = open('input.txt')

def creating_cipther(arr):
    minus_num = 0

    while True:
        # 첫 번째 숫자를 감소하고, 맨 뒤로 보낸다.
        num = arr.pop(0) - (minus_num % 5 + 1)
        arr.append(num)
        # 방금 감소한 값이 0 이하라면 종료
        if arr[-1] <= 0:
            arr[-1] = 0
            break

        minus_num += 1

    return arr


for _ in range(10):
    TC = int(input())
    arr = list(map(int, input().split()))

    answer = creating_cipther(arr)

    print('#{}'.format(TC), end=' ')
    for a in answer:
        print(a, end=' ')
    print()
