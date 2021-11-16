import sys
sys.stdin = open('input.txt')

T = int(input()) # 몇 번의 테스트 케이스가 있을지 입력받습니다.
for t in range(T):
    N = int, input()
    lst = list(map(int, input()))
    cnt_lst = [0] * 10
    for i in lst:
        cnt_lst[i] += 1 # 각 숫자가 몇 개 있는지 나타내는 cnt_lst를 만듭니다.

    temp_max = 0  # 가장 많이 나온 횟수를 저장합니다.
    temp_idx = 0  # 가장 많이 나온 숫자를 저장합니다.
    for idx, value in enumerate(cnt_lst): # index가 숫자와 같아서 그냥 enumerate을 썼습니다.
        if value >= temp_max:
            temp_max = value
            temp_idx = idx

    print('#{0} {1} {2}'.format(t + 1, temp_idx, temp_max))