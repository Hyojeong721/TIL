
import sys
sys.stdin = open('input.txt')

N = int(input())
q = []
for i in range (N):
    call_str = input()
    call = call_str[0]
    if call == 'c':
        print(len(q))
    elif call == 'o':
        if q:
            print(q.pop(0))
        else:
            print('empty')
    else:
        q.append(call_str[2:])

