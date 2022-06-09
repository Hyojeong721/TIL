T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    M = bin(M)
    result = 'ON'
    for i in range(len(M)-1, len(M)-N, -1):
        if M[i] == '0':
            result = 'OFF'
            break

    print(f'#{tc} {result}')