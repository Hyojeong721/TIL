import sys
sys.stdin = open('input.txt')

def is_matched(text):
    '''
    괄호가 올바르게 맞는지 판단하는 함수입니다.
    :param text:
    :return: Return True of all delimiters are properly match; False otherwise.
    '''

    lefty = '({['
    righty = ')}]'

    stack = []

    for char in text:             
        if char in lefty:
            stack.append(char)
        elif char in righty:
            # isEmpty
            if len(stack) == 0:
                return False
            if righty.index(char) != lefty.index(stack[-1]):
                return False
            if righty.index(char) == lefty.index(stack[-1]):
                stack.pop()

    if len(stack):
        return False
    else:
        return True
    
TC = int(input())

for tc in range(TC):
    text = list(input())
    is_matched(text)

    if is_matched(text) == True:
        result = 1
    if is_matched(text) == False:
        result = 0

    print("#{} {}".format(tc+1, result))

