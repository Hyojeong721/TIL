# 중위표기법에서 후위표기법으로

txt = '2+3*4/5'

stack = []
result = ''

for t in txt:
    if t.isnumeric():
        result += t
    else:
        stack.append(t)

while stack:
    result += stack.pop()

print(result)