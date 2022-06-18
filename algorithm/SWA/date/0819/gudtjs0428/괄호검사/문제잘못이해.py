import sys
sys.stdin = open('input.txt')

# input이 전부 괄호인줄 ㅋㅋ 게다가 쌍이 맞는지만 확인했었음

def if_pairs(pairs):
    while len(pairs):
        if pairs[0] == '}' or pairs[0] == ')':
            return 0
        elif pairs[0] == '{':
            check = 0
            for i in range(1, len(pairs)):
                if pairs[i] == '}':
                    del pairs[i], pairs[0]
                    check = 1
                    break
            if check == 0:
                return 0
        elif pairs[0] == '(':
            check = 0
            for i in range(1, len(pairs)):
                if pairs[i] == ')':
                    del pairs[i], pairs[0]
                    check = 1
                    break
            if check == 0:
                return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    pairs = list(input())
    print('#{} {}'.format(tc, if_pairs(pairs)))