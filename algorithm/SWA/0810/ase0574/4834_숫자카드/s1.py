import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers=[]
    number_list = [0]*10
    N = int(input())
    cards = list(map(str,input().split()))

    #카드 한장씩 분리 후, 숫자 갯수 리스트 채우기
    for i in cards:
        for j in range(len(i)):
            num = int(i[j])
            number_list[num] += 1

    #가장 많은 카드 골라서 카드번호(max_index)와 장수(max_number) 출력
    max_number = 0
    for i in range(10):
        if max_number < number_list[i]:
            max_number = number_list[i]
            max_index = i
        # 카드 장수가 동일할 경우 카드번호 높은 거 출력
        elif max_number == number_list[i]:
            max_number = number_list[i]
            max_index = i

    print('#{} {} {}'.format(tc, max_index, max_number))



