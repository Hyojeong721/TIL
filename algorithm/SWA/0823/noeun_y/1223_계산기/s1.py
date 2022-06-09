import sys
sys.stdin =open('input.txt')

for tc in range(1,11):
    n = int(input())
    str1=input()
    stack=[]
    result = ""
    for i in str1:

        #48~57
        if 48<=ord(i) and ord(i)<=57:
            result+=i


        if i == "+":
            while stack:
                result+=stack.pop()
            stack.append(i)


        if i == "*":
            while stack and stack[-1]=="*":
                result+=stack.pop()
            stack.append(i)

    while stack:
        result+=stack.pop()


    print(result)
    ans=0
    stack=[]
    for i in result:
        # 48~57
        if 48 <= ord(i) and ord(i) <= 57:
            stack.append(int(i))
        if i =="*":
            stack.append(stack.pop()*stack.pop())

        if i=="+":
            stack.append(stack.pop()+stack.pop())

    print("#{} {}".format(tc, stack.pop()))