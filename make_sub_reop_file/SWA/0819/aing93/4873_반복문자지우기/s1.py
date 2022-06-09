import sys
sys.stdin = open("input.txt")

# 테스트 케이스 받아오기
T = int(input())
for tc in range(1, T+1):
    repeat = input()
    # stack 초기화
    stack = []
    for i in range(len(repeat)):
        # stack 비었거나 stack 마지막 값이 repeat 과 다를 경우 append
        if not stack or stack[-1] != repeat[i]:
            stack.append(repeat[i])
        elif stack[-1] == repeat[i]: # 즉, 연속반복
            stack.pop()
    print("#{} {}".format(tc, len(stack)))