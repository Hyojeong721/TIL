import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    data = list(input().split())[:-1]
    stack = []
    err = 0

    for d in data:
        # 토큰이 숫자 형태인 경우
        if d.isnumeric():
            stack.append(d)  # stack에 추가

        else:
            # 연산
            try:
                # num2, num1 순서 주의!!!
                num2 = int(stack.pop())   # stack의 마지막 토큰
                num1 = int(stack.pop())   # stack의 마지막에서 두번째 토큰

                if d == '+': tmp = num1 + num2
                elif d == '-': tmp = num1 - num2
                elif d == '*': tmp = num1 * num2
                elif d == '/': tmp = num1 // num2

                stack.append(tmp)

            # 연산에 오류가 나는 경우
            except:
                err = 1

    # stack의 길이가 1이며 error가 발생하지 않은 경우
    if len(stack) == 1 and err == 0:
        result = stack[-1]   # 연산결과를 result에 저장

    # 문자열에 숫자만 있는 경우 error 반환
    else:
        result = 'error'

    print('#{} {}'.format(t, result))