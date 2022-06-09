import sys
sys.stdin = open('input.txt')

# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때,
# 수열의 맨 앞에 있는 숫자를 출력하는 프로그램

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    queue = []
    # 수열을 queue에 입력
    for i in range(N):
        queue.append(numbers[i])


    for i in range(M):
        front = queue.pop(0)
        queue.append(front)

    print("#{} {}".format(tc, queue[0]))
