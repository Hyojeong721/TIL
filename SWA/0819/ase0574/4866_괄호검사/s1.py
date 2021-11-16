import sys
sys.stdin = open('input.txt')

T = int(input())

G_open = ['(', '{']
G_close = [')', '}']

def check():
    for i in str1:
        if i in G_open:
            stack.append(i)
        elif i in G_close:
            if stack:
                a = stack.pop()
            else:
                return 0
            if a == "{" and i == ")":
                return 0
            if a == "(" and i == "}":
                return 0
    if stack:
        return 0
    else:
        return 1

for tc in range(1, T+1):
    str1 = input()
    stack = []
    print("#{} {}".format(tc, check()))





