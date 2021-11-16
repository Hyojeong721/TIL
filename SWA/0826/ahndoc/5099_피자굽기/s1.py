import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
# # 한번에 돌릴 수 있는 피자 인덱스를를 queue에 넣고 시작
    queue = list(range(N))   # enqueue

    while len(queue) != 1:
        i = queue.pop(0)     # dequeue

        C[i] //= 2

        if C[i] == 0:
            if N < M:
                queue.append(N)
                N += 1
        else:
            queue.append(i)

    result = queue[0] + 1
    print('#{} {}'.format(tc, result))




# 인덱스를 이용해서 피자를 굽자!
    # 치즈양 리스트 C의 인덱스를 피자 번호로 생각한다.
    # q를 인덱스 리스트로 만든다.
    # C에 인덱스로 접근한 후 C의 치즈양을 반씩 줄여준다.
    # 치즈양이 0이 되면 해당 피자 인덱스를 q에서 빼준다.
    # 남아있는 피자가 있다면 인덱스를 새로 추가한 후 피자를 다시 굽자!

    # q = list(range(N))
    #
    # while len(q) != 1:
    #     i = q.pop(0)
    #     C[i] //= 2
    #
    #     if C[i] == 0:
    #         if N < M:
    #             q.append(N)
    #             N += 1
    #     else:
    #         q.append(i)
    #
    # print(q)







