import sys
sys.stdin = open('input.txt')

T = 10 # 10개의 테스트 케이스
for tc in range(1, T+1):
    chance = int(input())  # 덤프 횟수
    lst = list(map(int, input().split()))
    total = sum(lst)
    quotient, remainder = divmod(total, 100)
    box_to_dump = sum(abs(i - quotient) for i in lst)
    print(box_to_dump - 2 * chance)
    if not remainder:
        box_to_dump = sum(abs(i - quotient) for i in lst)
        print(((box_to_dump - chance*2)//100 + 1)*2 + 1)

    # if remainder:
    #     higher = len([i for i in lst if i > quotient])
    #     if higher > remainder:
    #     for i in lst:
    #         if i > quotient:


