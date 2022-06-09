import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    front = 0
    rear = 7
    result = 1
    while True:
        for i in range(1, 6):
            if lst[front] - i <= 0:
                result = 0
                lst[front] = 0
                front = (front + 1) % 8
                rear = (rear + 1) % 8
                break

            else:
                lst[front] -= i
                front = (front + 1) % 8
                rear = (rear + 1) % 8

        if result == 0:
            break

    password = []
    for i in range(front, 8):
        password.append(str(lst[i]))
    for j in range(0, front):
        password.append(str(lst[j]))

    print('#{} {}'.format(tc, ' '.join(password)))