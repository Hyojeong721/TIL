import sys
sys.stdin = open('input.txt')

def post_fix_calculater(opers):
    nums = []
    operators = []
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
    for oper in opers:
        if 57 >= ord(oper) >= 48:
            nums += oper
        else:
            if oper != ')':
                if not operators:
                    operators.append(oper)
                else:
                    if icp[oper] > isp[operators[-1]]:
                        operators.append(oper)
                    else:
                        while operators and icp[oper] <= isp[operators[-1]]:
                            expression += operators.pop()
                        operators.append(oper)
            else:
                while operators[-1] != '(':
                    expression += operators.pop()
                operators.pop()

    return expression


T = 10
for test_case in range(1, T + 1):
    input()
    opers = input()
    print(eval(opers))