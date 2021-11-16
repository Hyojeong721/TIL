import sys
sys.stdin = open('input.txt')

def run_test(count):
    for i in range(8): # 마지막 검사 7, 8, 9
        if count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:
            return 1
    return 0

def game():
    # 1번 사람의 카운팅 정보
    count1 = [0] * 10
    # 2번 사람의 카운팅 정보
    count2 = [0] * 10
    for i in range(12): # 총 카드는 12장
        n = arr[i]
        if i % 2 == 0: # 1번 사람
            # 카운팅
            count1[n] += 1
            # triplet 검사
            if count1[n] == 3:
                return 1
            # run 검사
            if run_test(count1):
                return 1
        else:           # 2번 사람
            count2[n] += 1
            # triplet 검사
            if count2[n] == 3:
                return 2
            # run 검사
            if run_test(count2) == 1:
                return 2
    return 0 # 승자가 없는 경우

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print('#{} {}'.format(tc, game()))

