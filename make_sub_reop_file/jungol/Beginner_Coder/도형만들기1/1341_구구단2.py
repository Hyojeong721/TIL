s, e = map(int, input().split())

while not(2 <= s <= 9 and 2 <= e <=9):
    print("INPUT ERROR!")
    s, e = map(int, input().split())

if 2 <= s <= 9 and 2 <= e <=9:
    if s < e:
        small = s
        big = e

        for k in range(small, big+1): #작은덩어리에 큰덩어리로
            cnt = 1
            for i in range(3): #행  1, 2, 3
                for j in range(1, 4):
                    print(k, '*', cnt, '=', '%2d'%(k*cnt), end='   ')
                    cnt+=1
                print()
            print()
    else:
        small = e
        big = s
        for k in range(big, small - 1, -1):  # 작은덩어리에 큰덩어리로
            cnt = 1
            for i in range(3):  # 행  1, 2, 3
                for j in range(1, 4):
                    print(k, '*', cnt, '=', '%2d' % (k * cnt), end='   ')
                    cnt += 1
                print()
            print()