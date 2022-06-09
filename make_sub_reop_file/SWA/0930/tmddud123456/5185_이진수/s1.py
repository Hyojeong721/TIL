import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N, N16 = list(map(str, input().split()))
    N = int(N)
    answer = ''
    for i in range(N):
        temp = format(int(N16[i], 16), 'b')
        while len(temp) != 4:
            temp = '0' + temp
        answer += temp
        # else:
        #     if N16[i] == 'A':
        #         temp = str(format(10, 'b'))
        #         answer += temp
        #     elif N16[i] == 'B':
        #         temp = str(format(11, 'b'))
        #         answer += temp
        #     elif N16[i] == 'C':
        #         temp = str(format(12, 'b'))
        #         answer += temp
        #     elif N16[i] == 'D':
        #         temp = str(format(13, 'b'))
        #         answer += temp
        #     elif N16[i] == 'E':
        #         temp = str(format(14, 'b'))
        #         answer += temp
        #     elif N16[i] == 'F':
        #         temp = str(format(15, 'b'))
        #         answer += temp
        #     else:
        #         pass
    print(f'#{tc} {answer}')