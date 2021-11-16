import sys
sys.stdin = open('input.txt')

T = int(input())

def pages(P, target):
    start = 1
    end = P
    c = P // 2
    cnt = 1
    while ((start+end) // 2) != target:
        c = (start+end) // 2
        if start == end:
            break
        elif c > target:
            end = c
        else:
            start = c
        cnt += 1
    return cnt


for tc in range(1, T + 1):
    P, Pa, Pb = list(map(int, input().split()))
    if pages(P, Pa) < pages(P, Pb):
        print('#{} A'.format(tc))

    elif pages(P, Pa) > pages(P, Pb):
        print('#{} B'.format(tc))

    else:
        print('#{} 0'.format(tc))
