import sys
sys.stdin = open("input.txt")

n = input()
stack=[]
for i in n:
    #48~57
    if 48<=ord(i) and ord(i)<=57:
        print(i,end=" ")
    else:
        stack.append(i)

while stack:
    print(stack.pop(),end=" ")