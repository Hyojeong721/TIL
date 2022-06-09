import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    str1=input()
    stack=[]
    for i in str1:

        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    print("#{} {}".format(tc, len(stack)))