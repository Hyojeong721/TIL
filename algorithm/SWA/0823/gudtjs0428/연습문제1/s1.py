def post_fix_calculater(opers):
    expression = ''
    operators = []
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
    for oper in opers:
        if 57 >= ord(oper) >= 48:
            expression += oper
        else:
            if oper != ')':
                if not operators:
                    operators.append(oper)
                else:
                    if icp[oper] > isp[operators[-1]]:
                        operators.append(oper)
                    else:
                        while icp[oper] <= isp[operators[-1]]:
                            expression += operators.pop()
                        operators.append(oper)
            else:
                while operators[-1] != '(':
                    expression += operators.pop()
                operators.pop()

    return expression

opers = '(6+5*(2-8)/2)'
print(post_fix_calculater(opers))