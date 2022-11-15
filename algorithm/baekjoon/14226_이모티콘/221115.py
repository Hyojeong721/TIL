import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
ques = deque()
ques.append((1, 0, 0,'시작'))
ans = 1e9
temp = [[-1]*(N+1) for _ in range(N+1)]
temp.append((1, 0))
while ques:
    arr, que, res, ca = ques.popleft()
    if arr == N:
        ans = res
        break

    # 복사
    if arr != que:
        if temp[arr][arr] == -1:
            temp[arr][arr] = 1
            ques.append((arr, arr, res+1, '복사'))

    # 삭제
    if arr >= 2:
        if arr-1 > 0 and temp[arr-1][que] == -1:
            temp[arr - 1][que] = 1
            ques.append((arr-1, que, res+1, '삭제'))

    # 붙여넣기
    if que != 0:
        if arr+que <=N and temp[arr+que][que] == -1:
            temp[arr + que][que] = 1
            ques.append((arr+que, que, res+1, '붙여'))

print(ans)