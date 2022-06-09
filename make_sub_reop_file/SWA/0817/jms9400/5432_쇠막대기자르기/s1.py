import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = input()
    stick = 0
    result = 0 # 막대기 개수
    i = 0

    while i < len(arr):
        # 잘리는 부분
        if i != len(arr)-2 and arr[i] == '(' and arr[i+1] == ')':
            if stick > 0:
                result += stick
            i += 2
        # 막대가 생성되는 부분
        else:
            if arr[i] == '(':
                stick += 1
            else:
                stick -= 1
                result += 1
            i += 1
    print('#{} {}'.format(tc, result))
