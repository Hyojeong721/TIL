import sys
sys.stdin = open("input.txt", "r")



TC = int(input())

for tc in range(TC):

    N = int(input())
    box = list(map(int, input().split()))


    def gravity(N, box):
        result = 0
        for i in range(N):
            count = 0
            for j in range(i + 1, N):
                if box[i] <= box[j]:
                    count += 1
            temp = N - i - 1 - count

            if temp > result:
                result = temp

        print(result)

    gravity(N, box)


