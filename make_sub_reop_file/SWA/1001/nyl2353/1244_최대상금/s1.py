'''

get(key[, default])

    key가 딕셔너리에 있는 경우 key에 대응하는 값을 돌려주고, 그렇지 않으면 default 를 돌려준다.
    default 가 주어지지 않으면 기본값 None 이 사용된다.
    이 메서드는 절대로 KeyError를 일으키지 않는다.

'''
import sys
sys.stdin = open('input.txt')


def dfs(cnt):
    global ans

    # 횟수 다 사용했으면 검사
    if not cnt:
        temp = int(''.join(numbers))
        if ans < temp:
            ans = temp
        return

    # 모든 자리랑 바꿔보며 재귀적으로 내려감
    for i in range(length):
        for j in range(i+1, length):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            temp = ''.join(numbers)
            if not visited.get((temp, cnt-1), 0):
                visited[(temp, cnt-1)] = 1
                dfs(cnt-1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for tc in range(1, T + 1):
    # 자료형 정리
    numbers, exchange = input().split()
    numbers = list(numbers)
    exchange = int(exchange)

    ans = -1
    length = len(numbers)
    visited = {}    # 같은 교환횟수일 때 이미 나온 수라면 넘어가기 위해 저장
    dfs(exchange)
    print('#{} {}'.format(tc, ans))
