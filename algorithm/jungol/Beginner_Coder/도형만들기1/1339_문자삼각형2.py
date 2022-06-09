N = int(input())  #5
arr = [[0]*N for _ in range(N)]

if N % 2 and 1 <= N <= 100:
    cnt = 65
    half = N // 2
    for col in range(half, -1, -1):
        end = int(N / 2 * 2 - col)
        for row in range(col, end):
            if cnt == 91:
                cnt = 65
            arr[col][row] = chr(cnt)
            cnt += 1

    for i in range(N):
        for j in range(N):
            if arr[j][i] == 0:
                print(' ', end=' ')
            else:
                print(arr[j][i], end=' ')
        print()
else:
    print("INPUT ERROR")
