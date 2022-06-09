import sys
sys.stdin = open('input.txt')

T = int(input())

def check_str(lst):
    table = []
    for s in lst:
        if s == '(':
            table.append(s)
        elif s == '{':
            table.append(s)
        elif s == ')':
            if table.pop() != '(':
                return 0
        elif s == '}':
            if table.pop() != '{':
                return 0
    if len(table) == 0:
        return 1
    else:
        return 0

for tc in range(1, T + 1):
    str_lst = input()

    print('#{} {}'.format(tc, check_str(str_lst)))