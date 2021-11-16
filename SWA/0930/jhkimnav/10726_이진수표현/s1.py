import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    ans = ''
    for i in range(N):
        # 1을 i번 왼쪽 시프트 시킨수와 M을 and 연산한 결과가 1 이상 이면
        # 끝에서부터 i번째 비트가 1이라는 의미이고, 이때 cnt 를 1 증가
        # 이렇게 N번 반복해서 N개의 비트를 검사하고, 나온 카운트횟수가
        # N이랑 같다면 모두 켜져있기 때문에 ON 이고, 그게 아니라면 OFF
        if M & (1 << i):
            cnt += 1

    if N == cnt:
        ans = 'ON'
    else:
        ans = 'OFF'
    print('#{} {}'.format(tc, ans))

