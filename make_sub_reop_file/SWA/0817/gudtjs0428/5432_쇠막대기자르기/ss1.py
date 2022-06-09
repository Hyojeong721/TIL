import sys
sys.stdin = open('input.txt')

def break_steels(steels_w_lazers):
    stack = 0
    sticks = 0
    for i in range(len(steels_w_lazers)):
        if steels_w_lazers[i] == '(':
            stack += 1
        if steels_w_lazers[i] == ')':
            if steels_w_lazers[i-1] == '(':
                stack -= 1
                sticks += stack
            else:
                stack -= 1
                sticks += 1
    return sticks


T = int(input())
for test_case in range(1, T + 1):
    steels_w_lazers = input()
    print('#{} {}'.format(test_case, break_steels(steels_w_lazers)))