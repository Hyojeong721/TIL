import sys
sys.stdin = open("input.txt")

def delOverlap(chrs):
    '''
    중복 문자를 제거하는 함수입니다.
    :param chrs:
    :return: 중복 문자가 제거된 문자열 리스트를 반환합니다.
    '''

    stack = []

    for i in range(len(chrs)):
        # isEmpty
        if len(stack) == 0:
            # push
            stack.append(chrs[i])
        else:
            if stack[-1] == chrs[i]:
                stack.pop()
            else:
                stack.append(chrs[i])
    return stack

T = int(input())

for tc in range(1, T + 1):
    chrs = list(input())
    result = len(delOverlap(chrs))

    print("#{} {}".format(tc, result))
