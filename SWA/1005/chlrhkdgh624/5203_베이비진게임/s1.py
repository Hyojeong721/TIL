import sys
sys.stdin = open('input.txt', 'r')


def run_check(arr):
    for num in range(8):
        if num in arr:
            if num+1 in arr:
                if num+2 in arr:
                    return 1
    return 0


def triplet(arr):
    for num in range(10):
        if arr.count(num) == 3:
            return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    cards.reverse()
    score1 = 0
    score2 = 0
    first = []
    second = []
    result = 0
    while cards:
        first.append(cards.pop())
        score1 += run_check(first) + triplet(first)
        if score1 > 0:
            result = 1
            break
        second.append(cards.pop())
        score2 += run_check(second) + triplet(second)
        if score2 > 0:
            result = 2
            break

    print(f'#{tc} {result}')
