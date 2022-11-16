import sys
input = sys.stdin.readline
from collections import deque

que = deque()
N = int(input())
K = int(input())
que.append((N, 0))
visitied = [False] * 1024
change = {'0':'1', '1':'0'}
visitied[int(str(N), 2)] = True
res = 0
# 10->2 : bin / 2->10 int('str', 2)
# que에는 2진수 int 형태로 저장
while que:
    now, cnt = que.popleft()
    if now == str(K):
        res = cnt
        break
    # 한 자리 숫자를 보수로 바꾸기.단, 맨 앞숫자(MostSignificant Digit)는 바꿀 수 없다.
    now_str = str(now)
    for k in range(1, len(now_str)):
        temp_2_str = now_str[:k] + change[now_str[k]] + now_str[k+1:]
        temp_10 = int(temp_2_str, 2)
        if not visitied[temp_10]:
            visitied[temp_10] = True
            que.append((temp_2_str, cnt+1))

    # 현재    수에    1    더하기.
    temp = int(now_str, 2)
    if temp+1 < 1024 and not visitied[temp+1]:
        visitied[temp+1] = True
        que.append((str(bin(temp+1)[2:]), cnt+1))
    #  현재    수에서    1    빼기.단, 현재    수가    0    이라면    빼기가    불가능하다.
    if temp-1 > 0 and not visitied[temp-1]:
        visitied[temp-1] = True
        que.append((str(bin(temp - 1)[2:]), cnt + 1))


print(res)