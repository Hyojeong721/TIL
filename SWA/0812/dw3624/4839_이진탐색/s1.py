import sys
sys.stdin = open('input.txt')

T = int(input())

def page_search(page):
    cnt = 1
    c = int((1 + p) / 2)
    l, r = 1, p
    while c != page:
        if page == c:
            break
        elif page < c:
            r = c
        elif page > c:
            l = c
        cnt += 1
        c = int((l + r) / 2)
    return cnt


for t in range(1, T + 1):
    p, pa, pb = map(int, input().split())

    cnts = [page_search(pa), page_search(pb)]

    if cnts[0] == cnts[1]:
        result = 0
    elif cnts[0] < cnts[1]:
        result = 'A'
    elif cnts[0] > cnts[1]:
        result = 'B'

    print("#{} {}".format(t, result))
