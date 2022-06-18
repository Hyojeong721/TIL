import sys
sys.stdin = open('input.txt')


def search(n):
    if n <= N:
        search(2*n)
        search(2*n+1)
        tree_list.append(tree[n])
    return tree_list

def cal():
    for i in range(N):
        if tree_list[i] in ['-', '+', '*', '/']:
            b = float(result.pop(-1))
            a = float(result.pop(-1))

            if tree_list[i] == '-':
                result.append(a-b)
            elif tree_list[i] == '+':
                result.append(a+b)
            elif tree_list[i] == '*':
                result.append(a*b)
            elif tree_list[i] == '/':
                result.append(a/b)

        else:
            result.append(tree_list[i])

    return result

T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0]
    tree_list= []
    result = []
    for n in range(N):
        arr = input().split()
        tree.append(arr[1])

    print(search(1))
    cal()
    print("#{} {}".format(tc, int(*result)))


