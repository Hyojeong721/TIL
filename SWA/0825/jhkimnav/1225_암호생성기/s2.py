# while 문 간소화
import sys
sys.stdin = open('input.txt')


def creating_cipther(arr):
    minus_num = 0

    # 배열의 맨 뒤 숫자가 0보다 크다면 감소 진행
    while arr[-1] > 0:
        # 배열의 맨 앞 숫자를 일정량 감소하고, 맨 뒤로 보낸다.
        num = arr.pop(0) - (minus_num % 5 + 1)
        arr.append(num)
        minus_num += 1

    arr[-1] = 0
    return arr


for _ in range(10):
    TC = int(input())
    arr = list(map(int, input().split()))

    answer = creating_cipther(arr)

    print('#{}'.format(TC), end=' ')
    for a in answer:
        print(a, end=' ')
    print()
