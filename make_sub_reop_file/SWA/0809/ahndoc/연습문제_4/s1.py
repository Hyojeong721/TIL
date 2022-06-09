import sys
sys.stdin = open("input.txt", "r")




TC = int(input())
for tc in range(TC):
    c = [0] * 10
    num = []
    for n in input():
        num.append(int(n))

    for i in num:
        c[i] += 1


    i = 0
    tri = run = 0
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2: print("Baby Gin")
    else: print("Lose")

