import sys
sys.stdin = open("input.txt")

# 집합 A의 부분집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합을 출력
# 해당 부분집합이 없는 경우 0 을 출력
# 부분집합의 원소의 수 N, 집합의 합 K

T = int(input())
N, K = map(int, input().split())

n = 12
result = 0

for tc in range(1, T+1):

    for i in range(1 << n): # 부분집합의 총갯수
        cnt_count, cnt_total = 0, 0
        for j in range(n) : # 원소의 수만큼 비트를 비교
            if i & (1 << j): # i의 j번째 비트가 1인 경우
                cnt_count += 1
                cnt_total += (j + 1)

        if cnt_count == N and cnt_total == K:
            result += 1

    print("#{} {}".format(tc, result))





# # 방법 1
# n, m = map(int, input().split())
# mylist = [0 for _ in range(n)]
# for i in range(n):
#     mylist[i] = list(map(int,input().split()))
#
#
# print(mylist)