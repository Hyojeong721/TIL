# s(구간처음),e(구간끝)
s, e = map(int, input().split())

while not(2 <= s <= 9 and 2 <= e <=9):
    print("INPUT ERROR!")
    s, e = map(int, input().split())

if 2 <= s <= 9 and 2 <= e <=9:
    if s < e:
        for i in range(1, 10): #행
            for j in range(s, e+1):
                print(j, '*', i, '=', '%2d' %(j*i), end='   ')
            print()
    else:
        for n in range(1, 10): #행
            for m in range(s, e-1, -1):
                print(m, '*', n, '=', '%2d' %(m*n), end='   ')
            print()

