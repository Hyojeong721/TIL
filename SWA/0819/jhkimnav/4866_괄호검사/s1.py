import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    answer = True
    search_str = input()
    stack = []
    for i in range(len(search_str)):
        # 여는 대괄호 { 를 만나면 닫는 }를 push, (
        if search_str[i] == '{':
            stack.append('}')
        elif search_str[i] == '(':
            stack.append(')')

        elif search_str[i] == '}' or search_str[i] == ')':
            # 스택이 비어있을 경우
            if len(stack) == 0:
                answer = False
                break
            last_c = stack.pop()
            # 짝이 맞지 않다면 탐색 종료
            if search_str[i] != last_c:
                answer = False
                break

        # 마지막까지 검사하고, stack에 무언가가 남았다면 0
        if i == len(search_str)-1 and len(stack) > 0:
            answer = False
    print('#{} {}'.format(TC, int(answer)))