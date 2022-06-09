n, m = map(int, input().split())

arr = [([0]*m) for _ in range(n)]
cnt = 1

for i in range(n):
    # 홀수행
    if i % 2:
        # 오른쪽에서 왼쪽으로 채우기
        for j in range(m-1, -1, -1):
            arr[i][j] = cnt
            cnt += 1
    # 짝수행
    else:
        # 왼쪽에서 오른쪽으로
        for j in range(m):
            arr[i][j] = cnt
            cnt += 1

for s in range(n):
    for q in range(m):
        print(arr[s][q], end=' ')
    print()
