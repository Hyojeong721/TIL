import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    text = []
    for _ in range(N):
        text.append(list(''.join(input())))

    result = []

    # 가로 방향
    for row in range(N):
        for col in range(N-M+1):
            palindrome = text[row][col:col+M]
            palindrome_reverse = [palindrome[x] for x in range(M-1, -1, -1)]
            check = [palindrome[i] for i in range(M) if palindrome[i] != palindrome_reverse[i]]
            if len(check) == 0:
                result.append(''.join(palindrome))

    # 세로 방향
    for col in range(N):
        for row in range(N-M+1):
            palindrome = ''
            for j in range(row, row + M):
                palindrome += text[j][col]
            palindrome_reverse = [palindrome[x] for x in range(M - 1, -1, -1)]
            check = [palindrome[i] for i in range(M) if palindrome[i] != palindrome_reverse[i]]
            if len(check) == 0:
                result.append(''.join(palindrome))

    print(f'#{tc} {result[0]}')


