import sys
sys.stdin = open('input.txt')

# idea
# 한글자씩 stack에 추가
## stack[-1]와 같은 글씨 나왔을 경우
## stack.pop 후 다음 글씨로

T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []   # 빈 stack : 글자를 하나씩 뽑아 보관하기 위함
    idx = 0   # 인덱스 : text에서 글자를 하나씩 뽑기 위함

    while idx < len(text):  # text의 모든 글자를 조사
        t = text[idx]   # text의 idx번째 글자를 t로 지정

        # stack이 비어있지 않고 마지막 글자가 t와 같은 경우
        if len(stack) > 0 and stack[-1] == t:
            stack.pop()   # stack에서 마지막 글자 제거

        # 마지막 글자가 t와 다른 경우
        else:
            stack.append(t)  # stack에 t 추가

        idx += 1   # 다음 index로
        # print('t:', t, ' stack:', stack)   # 현재 글자와 stack 확인용

    print('#{} {}'.format(tc, len(stack)))