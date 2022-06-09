import sys
sys.stdin = open('input.txt')

# 맨 앞 숫자 pop
# n 감소
## 숫자가 0 이하인 경우 종료
## 숫자가 0 이상인 경우 push
# n += 1
# n == 5인 경우 cycle 종료


T = 10
for i in range(1, T+1):
    tc = int(input())
    que = list(map(int, input().split()))
    n = 1

    while que[-1] > 0:
        num = que.pop(0)
        num -= n

        # 숫자가 0 이하인 경우 반복문 종료
        if num <= 0:
            que.append(0)
            break

        # queue에 숫자 추가, n 1 추가
        else:
            que.append(num)
            n += 1

        # 사이클 종료, n 초기화
        if n == 6:
            n = 1

    print('#{}'.format(tc), end = ' ')
    print(*que)