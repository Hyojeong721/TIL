import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    queue = list(map(int, input().split()))
    i = 1

    while queue[-1] > 0:
        front = queue.pop(0)     # 맨 앞 숫자 가져오기
        rear = front - i         # 맨앞에 숫자에서 -i
        i += 1
        if i == 6:               # 한 사이클(1 <= i <=5) 끝나면
            i = 1                   # 다시 i=1로
        if rear <= 0:            # 뺀 결과가 0이거나 음수이면
            rear = 0             # 0으로 저장
        queue.append(rear)       # 결과는 맨뒤로 이동

    print('#{}'.format(tc), end= ' ')
    print(*queue)
