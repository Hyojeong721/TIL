TC = int(input())

for tc in range(TC):
    n = int(input())
    if n == 0:
        print(0)
    else:
        closet = {}
        for row in range(n):
            cus, cate = input().split()
            if cate not in closet:
                closet[cate] = 2
            else:
                closet[cate] = closet[cate] + 1

        res = 1
        for cnt in closet.values():
            res *= cnt

        print(res-1)