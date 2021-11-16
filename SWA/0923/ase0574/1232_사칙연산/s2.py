import sys
sys.stdin = open('input.txt')

def postorder(node): #후위표기식
    if 0 < node <= V:
        postorder(left[node])
        postorder((right[node]))
        equation.append(tree[node])


def calculator(a,b,x):
    if x == '+':
        return a + b
    elif x == '-':
        return a - b
    elif x == '*':
        return a * b
    elif x == '/':
        return a / b


for tc in range(1,11):
    V = int(input())
    left = [0]*(V+1)
    right = [0]*(V+1)
    tree = [0]*(V+1)
    equation = []


    for _ in range(V):
        tmp = input().split()
        if len(tmp) == 4:
            left[int(tmp[0])] = int(tmp[2])
            right[int(tmp[0])] = int(tmp[3])
            tree[int(tmp[0])] = tmp[1]
        else:
            tree[int(tmp[0])] = int(tmp[1])


    postorder(1)

    stack = []

    for num in equation:
        if type(num) != int:
            b = stack.pop()
            a = stack.pop()
            c = calculator(a,b,num)
            stack.append(c)
        else:
            stack.append(num)

    answer = int(stack.pop())

    print('#{} {}'.format(tc, answer))