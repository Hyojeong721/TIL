import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N_lst = []
    N_lst.extend(input()) # N의 각 문자를 원소로 하는 리스트를 입력합니다.
    N = list(set(N_lst)) # 중복 계산을 막기 위해 set을 이용하여 중복된 원소를 하나만 남깁니다.
    M = input()
    result = {} # 결과를 저장하기 위한 딕셔너리를 만듭니다.
    for i in M:
        if i in N:
            result[i] = result.get(i, 0) + 1 # M의 각 원소를 순회하며 카운트한 결과를 N을 key로 갖는 딕셔너리에 저장합니다,.
    total = 0
    for value in result.values(): # value 중 가장 큰 값을 찾습니다.
        if value > total:
            total = value

    print('#{} {}'.format(tc, total))