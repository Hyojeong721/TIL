import sys
sys.stdin = open('input.txt')


T = int(input())

for t in range(T):
    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    temp_min = sum(lst[:M]) # 현재까지의 최솟값을 저장합니다. sum 함수 써서 죄송합니다...
    temp_max = sum(lst[:M]) # 현재까지의 최댓값을 저장합니다.
    for j in range(N-M+1): # list index error를 방지하기 위해 range를 축소합니다.
        total = sum(lst[j:j + M]) 
        if total > temp_max: # 기존의 최댓값보다 크면 최댓값을 업데이트합니다.
            temp_max = total
        elif total < temp_min: # 기존의 최솟값보다 작으면 최솟값을 업데이트합니다.
            temp_min = total

    print('#%s' % (t + 1), temp_max - temp_min)