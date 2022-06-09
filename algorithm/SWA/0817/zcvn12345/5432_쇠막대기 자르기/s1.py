import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = input()
    stick = 0
    result = 0
    for i in range(len(arr)):
        # 막대기가 나타남
        if arr[i] == '(' and arr[i+1] != ')':
            stick += 1
            result += 1
        # 레이저가 나타남
        elif arr[i] == '(' and arr[i+1] == ')':
            result += stick
        # 막대기 끝
        elif arr[i-1] != '(' and arr[i] == ')':
            stick -= 1
    print('#{0} {1}'.format(tc, result))

