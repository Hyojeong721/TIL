import sys
sys.stdin = open('input.txt')

T = int(input())
arr = [[0]*5 for i in range(5)]
print(arr)
for x in range(len(arr)):
    N = int(input())
    # arr = list(map(int, input().split()))
    print(arr)
# dx=[0,0,-1,1] #상하좌우
# dy=[-1,1,0,0]
# #델타 값을 이용하여 특정 원소의 상하좌우에 위치한 원소에 접근할 수 있음
#
# for x in range(len(arr)):
#     for y in range(len(arr[x])):
#         for i in range(4):
#             testX=x+dx[i]
#             testY=y+dy[i]
#             print(arr[testX][testY])