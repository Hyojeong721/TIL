import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    stack=[]
    for i in input().split():

        if len(i)>1:
            stack.append(int(i))
        elif 48<=ord(i) and ord(i)<=57:
            stack.append(int(i))

        elif len(stack)>=2:
            a=stack.pop()
            b=stack.pop()
            if i =="+":
                stack.append(b+a)
            elif i =="*":
                stack.append(b*a)
            elif i =="/":
                stack.append(b//a)
            elif i =="-":
                stack.append(b-a)
            else:
                print("#{} error".format(tc))
                break

        elif i =='.':
            if len(stack)==1:
                print("#{} {}".format(tc,stack.pop()))
        else:
            print("#{} error".format(tc))
            break



