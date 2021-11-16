import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    stick = input()
    stick = stick.replace('()', '*')
    answer = 0
    cnt = 0
    for s in stick:
        if s == '*':
            answer += cnt
        elif s == '(':
            cnt += 1
        else:
            cnt -= 1
            answer += 1

    print(f'#{test_case} {answer}')