import sys
sys.stdin = open('input.txt')

T = int(input())
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T + 1):
    input()
    lst = input().split()
    for idx, value in enumerate(lst): # 스트링을 숫자로 바꾸는 작업입니다.
        for i, j in enumerate(numbers):
            if j == value: # 약간의 낭비가 있는 부분이지만,,,
                lst[idx] = i
                break
    lst.sort()
    for idx, value in enumerate(lst): # 숫자를 다시 스트링으로 바꾸는 작업입니다.
        lst[idx] = numbers[value]

    lst = ' '.join(lst)

    print('#{} {}'.format(tc, lst))