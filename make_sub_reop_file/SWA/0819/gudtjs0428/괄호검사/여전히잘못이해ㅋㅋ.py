import sys

sys.stdin = open('input.txt')

# 여전히 input이 전부 괄호인줄

def if_match(brackets):
    checking = brackets[:]
    i = 0
    while i < len(checking) - 1:
        if checking[i] == '(' and checking[i+1] == ')':
            checking = checking[:i] + checking[i+2:]
            i = 0
        elif checking[i] == '{' and checking[i+1] == '}':
            checking = checking[:i] + checking[i + 2:]
            i = 0
        else:
            i += 1

    if checking:
        return 0
    else:
        return 1
T = int(input())
for tc in range(1, T + 1):
    brackets = input()
    print('#{} {}'.format(tc, if_match(brackets)))