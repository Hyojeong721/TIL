import sys
import re
sys.stdin = open('input.txt')

T = int(input())

def check_str(lst):
    table = []
    if len(lst) % 2:
        return 0
    else:
        for s in lst:
            if s in '({':
                table.append(s)
            elif s == ')':
                if table.pop() != '(':
                    return 0
            else:
                if table.pop() != '{':
                    return 0
        if len(table) == 0:
            return 1
        else:
            return 0

for tc in range(1, T + 1):
    str_lst = input()
    lst = re.findall('[(){}]', str_lst)

    print('#{} {}'.format(tc, check_str(lst)))
