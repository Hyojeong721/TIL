import sys
sys.stdin = open("input.txt")

# N개의 숫자로 이루어진 수열
# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 수행
# 수열의 맨 앞에 있는 숫자를 출력

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    for i in range(M):
        popped = data.pop(0)
        data.append(popped)

    print("#{} {}".format(tc, data[0]))


######################################################
# while로 푼 경우

# T = int(input())
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     data = list(map(int, input().split()))
#     cnt = 0
#
#     while cnt < M:
#         tmp = data.pop(0)
#         data.append(tmp)
#         cnt += 1
#
#     print('#{} {}'.format(t, data[0]))