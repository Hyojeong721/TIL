import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     result = []
#     for i in range(0, N-M+1):
#         temp = 0
#         for j in range(0, M):
#             temp += numbers[i+j]
#         result.append(temp)
#
#     max = result[0]
#     min = result[0]
#     for i in result:
#         if i > max:
#             max = i
#         elif i < min:
#             min = i
#
#     print('#{} {}'.format(tc, max-min))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    result=[]
    for i in range(N-M+1):
        temp=0
        for j in range(M):
            temp += lst[j+i]
        result.append(temp)

    print(result)




