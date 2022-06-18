import sys
sys.stdin = open('input.txt')


def delete_repeat(word):
    """
    문자열을 인자로 받아, 반복문자를 지운 문자열을 구한다.
    (ex. CAAABBA => CABBA => CAA => C)

    Returns:
        반복 문자를 제거한 문자열
    """
    stack = []

    for char in word:
        # 스택이 비어있지 않고, 현재 문자가 스택의 마지막 문자와 같다면
        if stack and char == stack[-1]:
            stack.pop()
        # 스택이 비어있거나, 현재 문자가 스택의 마지막 문자와 다르다면
        else:
            stack.append(char)

    return ''.join(stack)


T = int(input())

for tc in range(1, T + 1):
    new_word = input()
    repeat_deleted_word = delete_repeat(new_word)

    print("#{} {}".format(tc, len(repeat_deleted_word)))
