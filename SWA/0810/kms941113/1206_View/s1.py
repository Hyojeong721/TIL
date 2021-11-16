import sys
sys.stdin = open("input.txt", "r")

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    heights = list(map(int,input().split()))
    view = 0

    for i in range(2, N-2):
        min_value = 987654321
        for j in range(5):
            if j != 2:
                if heights[i] - heights[i-2+j] < min_value:
                    min_value = heights[i] - heights[i-2+j]
        if min_value > 0 :
            view += min_value
    print("#{} {}".format(tc, view))