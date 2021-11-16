import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
#K : 최대 이동 가능 수
#N : 종점
#M : 충전기 정류장 수
    K, N, M = list(map(int, input().split()))
#charge : 충전기 위치
    charge = list(map(int,input().split()))+[N+K,N+K]
#현재 위치
    here = 0
#정류장 위치
    i = 0
#충전 할때마다 +1
    cnt = 0

while here + K<N:
    if here+K>=charge[i+2]:
        here = charge[i+2]
        cnt += 1
        i += 3
        continue

    elif here+K >= charge[i+1]:
        here = charge[i+1]
        cnt += 1
        i += 2
        continue

    elif here+K < charge[i]:
        cnt = 0
        break

    else:
        here = charge[i]
        cnt += 1
        i += 1

print("#%d %d"%(test_case, cnt))