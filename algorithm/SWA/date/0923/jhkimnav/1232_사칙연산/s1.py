import sys
sys.stdin = open('input.txt')


def calculate(operator):

    if operator == '+':
        num_2 = stack.pop()
        num_1 = stack.pop()
        stack.append(num_1 + num_2)
    elif operator == '-':
        num_2 = stack.pop()
        num_1 = stack.pop()
        stack.append(num_1 - num_2)
    elif operator == '*':
        num_2 = stack.pop()
        num_1 = stack.pop()
        stack.append(num_1 * num_2)
    elif operator == '/':
        num_2 = stack.pop()
        num_1 = stack.pop()
        stack.append(num_1 // num_2)


def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        if tree[n] in '+-*/':
            calculate(tree[n])
        else:
            stack.append(int(tree[n]))


T = 10
for TC in range(1, T+1):
    # N : 정점의 총 개수
    N = int(input())
    tree = ['0'] * (N + 1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    for _ in range(N):
        input_data = list(input().split())
        if len(input_data) == 2:
            tree[int(input_data[0])] = input_data[1]
        else:
            tree[int(input_data[0])] = input_data[1]
            left[int(input_data[0])] = int(input_data[2])
            right[int(input_data[0])] = int(input_data[3])

    stack = [0]
    total_value = 0
    post_order(1)
    print('#{} {}'.format(TC, int(stack.pop())))




