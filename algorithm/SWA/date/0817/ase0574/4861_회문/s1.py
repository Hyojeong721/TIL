import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    #N X N배열 / M = 회문의 길이
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))

    # row 검사
    for j in range(N-M+1):
        for i in arr:
            if i[j:M+j] == i[j:M+j][::-1]:
                print('#{} {}'.format(tc, i[j:j+M]))
                break

        #col 검사
    for col in range(N):
        temp = ''
        for row in range(N):
            temp += arr[row][col]
        for i in range(N // 2):
            if temp[i:M+i] == temp[i:i+M][::-1]:
                print('#{} {}'.format(tc, temp[i:i+M]))









