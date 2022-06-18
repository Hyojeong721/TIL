import sys
sys.stdin = open('input.txt')

arr = list(input())
# isp = {
#     '*': 2,
#     '/': 2,
#     '+': 1,
#     '-': 1,
#     '(': 0,
# }
#
# icp = {
#     '*': 2,
#     '/': 2,
#     '+': 1,
#     '-': 1,
#     '(': 3,
# }

stack = []  # 부호
result = ''

for i in arr:
    if i in '+*/-':
        stack.append(i)
    else:
        result += i

while len(stack):
    s = stack.pop()
    result += s

print(result)