# 예상 출력 결과 : 2345/*+

str1 = '2+3*4/5'
stack = []
for c in str1:
    if c in '+*/()':
        stack.append(c)
    else:
        print(c, end='')
while len(stack):
    print(stack.pop(-1), end='')