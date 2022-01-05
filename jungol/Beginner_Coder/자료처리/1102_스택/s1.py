import sys
sys.stdin = open('input.txt')

N = int(input())
s=[]
for i in range (N):
    call_str = input()
    call = call_str[0]
    if call == 'c':
        print(len(s))
    elif call == 'o':
        if s:
            print(s.pop())
        else:
            print('empty')
    else:
        s.append(call_str[2:])

