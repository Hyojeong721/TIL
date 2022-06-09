import sys
sys.stdin = open('input.txt')

def calc(v):
    if len(tree[v]) == 2:
        return int(tree[v][1])
    else:
        L = calc(int(tree[v][2]))
        R = calc(int(tree[v][3]))

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        else: return L/R



# def postorder(n):
#     if n:
#         postorder(left[n])
#
#         postorder(right[n])
#         v = tree[n]
#
#         if v == '+':
#             num2 = stack.pop()
#             num1 = stack.pop()
#             stack.append(num1 + num2)
#
#         elif v == '-':
#             num2 = stack.pop()
#             num1 = stack.pop()
#             stack.append(num1 - num2)
#         elif v == '*':
#             num2 = stack.pop()
#             num1 = stack.pop()
#             stack.append(num1 * num2)
#         elif v == '/':
#             num2 = stack.pop()
#             num1 = stack.pop()
#             stack.append(num1 / num2)
#         else:
#             stack.append(v)


T = 10
for tc in range(1):
    N = int(input())
    # tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    # edges = list(input().split() for _ in range(N))
    tree = [0] + list(input().split() for _ in range(N))
    # for edge in edges:
    #     if len(edge) == 4:
    #         p, cal, c1, c2 = edge
    #         tree[int(p)] = cal
    #         left[int(p)] = int(c1)
    #         right[int(p)] = int(c2)
    #     else:
    #         p, v = edge
    #         tree[int(p)] = int(v)
    # print(tree)
    print(calc(1))
    # stack = []
    # postorder(1)
    # print('#{} {}'.format(tc, int(stack[0])))
