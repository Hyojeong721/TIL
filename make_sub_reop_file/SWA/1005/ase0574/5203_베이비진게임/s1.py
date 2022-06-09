# 두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때
# 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

import sys
sys.stdin = open('input.txt')

T = int(input())
def test():

    return

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    par_1 = []
    par_2 = []

    # 한장씩 교대로 가져가며
    for i in range(len(arr)//2):
        par_1.append(i*2)
        par_2.append(i*2+1)
        # 베이비진 검사
        test()

