import sys
sys.stdin = open('input.txt')
#이진탐색
def find_page(P, Pab):
    l = 1
    r = P
    result = 0
    while l < r:
        c = int((l + r) / 2)
        if c == Pab:
            result += 1
            return result
        elif Pab > c:
            l = c
            result += 1
        else:
            r = c
            result += 1

T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    if find_page(P,Pa) > find_page(P,Pb):
        print('#{} B'.format(tc))
    elif find_page(P,Pa) == find_page(P,Pb):
        print('#{} 0'.format(tc))
    else:
        print('#{} A'.format(tc))
