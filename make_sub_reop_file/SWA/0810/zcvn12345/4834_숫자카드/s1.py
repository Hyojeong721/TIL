import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cards = input()
    # 각각의 숫자 i를 count[i] 위치에 저장
    count = [0] * 10
    # 각각의 숫자 i를 count[i] 위치에 저장하는 코드
    for i in range(N):
        count[int(cards[i])] += 1

    max_count = count[0]
    max_number = 0
    for number in range(10):
        if max_count <= count[number]:
            max_count = count[number]
            max_number = number

    print('#{0} {1} {2}'.format(test_case, max_number, max_count))