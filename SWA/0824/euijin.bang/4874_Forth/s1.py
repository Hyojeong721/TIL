import sys
sys.stdin = open("input.txt")

stack = []

T = int(input())


operator = '+-*/.'

for tc in range(1, T+1):
    code = list(input().split())

    for token in code:
        if token not in operator:
            stack.append(token)
            print(stack)

            if token in operator:
                result = int(stack.pop()) token int(stack.pop())
                print(result)



    # print("#{} {}".format(tc, ))