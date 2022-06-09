import sys
sys.stdin = open('input.txt')

def devide():
    global N
    answer = ''
    i = -1
    while N != 0.0:
        if i == -13:
            return 'overflow'
        if N - 2**i >= 0:
            N = N - 2**i
            answer += '1'
        else:
            answer += '0'
        i -= 1
    return answer

TC = int(input())

for tc in range(1, TC + 1):
    N = float(input())
    answer = devide()
    print(f'#{tc} {answer}')