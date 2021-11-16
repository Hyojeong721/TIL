import sys
sys.stdin = open("input.txt")

# 연산자 operator isp, icp
# icp(in-coming priority)
# isp(in-stack priority)

def post_fix_calculator(opers):
    expression = ''
    operators = []
    isp = {'*' : 2, '/': 2, '+': 1, '-' : 1, '(' : 0}
    icp = {'*' : 2, '/': 2, '+': 1, '-' : 1, '(' : 3}

    for token in opers:
        # 토큰이 숫자일 경우
        if 57 >= ord(token) >= 48:
        # 토큰이 숫자가 아닐 경우
        else:
            # 토큰이 닫는 괄호가 아닌 경우
            if token != ')':
                if not operators:
                   operators.append(token)
                else:
                    if icp[token] > isp[operators[-1]]:
                        operators.append(token)
                    else:
                        while icp[token] <= isp[operators[-1]]:
                            expression += operators.pop()
                        operators.append(token)
            # 토큰이 닫는 괄호인 경우
            else:
                while operators[-1] != '(':
                    expression += operators.pop()
                operators.pop()

    return expression

opers = '(6+5*(2-8)/2)'
print(post_fix_calculator(opers))




