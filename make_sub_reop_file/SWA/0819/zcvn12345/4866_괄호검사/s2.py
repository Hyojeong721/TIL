import sys
sys.stdin = open("input.txt")

T = int(input())

def solution(user_input):
    arr = []
    match_dict = {'}': '{', ')': '('}
    for s in user_input:
        if s == '(' or s == '{':
            arr.append(s)
        elif s == ')' or s == '}':
            if len(arr) == 0 or arr[len(arr) - 1] != match_dict[s]:
                return 0
            arr.pop()
    if len(arr) != 0:
        return 0

    return 1


for tc in range(1, T+1):
    C = input()

    print('#{0} {1}'.format(tc, solution(C)))