import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    chars = []
    result = ''
    for i in range(5):
        chars.append(input())
    for i in range(15):
        for j in chars:
            if i < len(j):
                result += j[i]
    print('#{0} {1}'.format(tc, result))