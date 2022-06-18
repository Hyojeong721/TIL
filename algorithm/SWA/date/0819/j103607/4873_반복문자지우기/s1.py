import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    string = list(input())

    result = []
    for i in string:
        if len(result) > 0 and i == result[-1]:
            result.pop()
        else:
            result.append(i)
    print('#{} {}'.format(tc, len(result)))