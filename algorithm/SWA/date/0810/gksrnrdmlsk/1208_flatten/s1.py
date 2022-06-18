import sys
sys.stdin = open('input.txt')

def dump(lst): # 덤프 동작 함수를 정의합니다.
    if max(lst) > min(lst):
        lst[lst.index(max(lst))] -= 1 # 최댓값을 가진 요소에 1을 뺍니다.
        lst[lst.index(min(lst))] += 1 # 최솟값을 가진 요소에 1을 더합니다.

T = 10 # 10개의 테스트 케이스
for tc in range(1, T+1):
    chance = int(input())  # 덤프 횟수
    lst = list(map(int, input().split()))
    for i in range(chance): # 횟수만큼 dump를 합니다.
        dump(lst)
    print('#{} {}'.format(tc, (max(lst) - min(lst))))