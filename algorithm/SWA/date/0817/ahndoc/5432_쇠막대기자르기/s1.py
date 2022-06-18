import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    pipe_data = input()
    # ()(((()())(())()))(())
    # (((()(()()))(())()))(()())
    # 파이프: () , 레이저: l
    # l(((ll)(l)l))(l)
    # (((l(ll))(l)l))(ll)
    pipe = pipe_data.replace('()', 'l')

    cnt = 0
    result = 0
    for i in pipe:
        if i == '(':
            cnt += 1

        elif i == ')':
            cnt -= 1
            result += 1

        elif i == 'l':
            result += cnt
    print('#{} {}'.format(tc, result))


