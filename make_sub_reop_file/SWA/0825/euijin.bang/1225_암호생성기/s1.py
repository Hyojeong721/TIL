import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):


    # 공백 큐 생성
    # Q = [0] * len(arr)
    # front = -1 # 인덱스 초기화
    # rear = -1

    Q = list(map(int, input().split()))
    front = -1
    rear = -1

    # 원소 삽입
    # enQueue(1번째 원소 삽입) => rear = -1 + 1
    # enQueue(2번째 원소 삽입) => rear = -1 + 1 + 1
    for i in range(8):
        rear = (rear+1) mod 5
        for i in range(1, 5):
            Q[len(arr)-1] = Q[front] - i
            break


    print(Q)

    # 원소 삭제 - 맨 앞 원소를 삭제하기 위해, front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소를 이동하고
    # 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능
    # for j in range(8):
    #     while arr[j] == 0: # 공백일 때까지 => 0일때까지
    #         front += 1
    #         for i in range(1, 5):
    #             Q[len(arr)-1] = Q[front] - i

