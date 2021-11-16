import sys
sys.stdin = open('input.txt')
"""
1. 모든 순서 구하기 -> 완전 검색
2. 탐욕 알고리즘 : 전체 중 가장 가치 있는 일부분을 처리,
나머지 값 중 또 가치가 있는 것들을 순차적으로 처리,
1) 각각의 카드 숫자를 센다.
   0~9 인덱스 배열에 
2) 앞쪽 인덱스부터 0이 아닌 다른 숫자가 포함되어 있으면, run/triplet 확인
triplet 부터 확인하는게 필요
3) 인덱스 배열이 모두 0으로 바뀌었다면, baby-gin!

4) run/triplet 검사를 많이 해야하기 때문에 검사 코드를 별도 함수로 작성

"""





# 베이비 진 >> run또는 triplet 확인
# run과 triplet 검사를 많이 해야 하기 때문에
# 검사 코드를 별도 함수로 작성
def check_run_triplet(arr):
    """
    :return: run이거나, triplet 이면,  1반환하기 아니면 0반환
    내가 가진 카드 덱의 순열을 이용한 run/triplet 확인이 아니라...
    각 카드를 몇장 가지고 있는가? 하는 배열을 이용한 확인
    arr : 0~9까지의 카드가 각 몇장씩 있는가 저장하는 배열

    """
    for i in range(8):
        if arr[i] >= 3:
            return 1
        if i <= 7 and arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            return 1
    return 0

T = int(input())
for tc in range(1,T+1):
    numbers = list(map(int,input().split()))
    # 각 플레이어가.... 돌아가면서 한 장씩 카드를 뽑기
    # 카드를 뽑을 때 마다 카드 덱이 run/ triplet인지 확인하기

    # 카드덱에서 한장씩 확인하면서, winner가 나오면 winner를 바꿔주면 됩니다.
    winner = 0  # 비기면, 0이니까. 0으로 초기화
    p1 = [0] * 10
    p2 = [0] * 10


    for i in range(0, len(numbers), 2):
        #카드 뽑으면서 승자가 나왔는지 확인
        #i 번째 카드가 p1의 카드 >> p1의 카드덱을 만들고
        p1[numbers[i]] += 1

        #check_run_triplet(p1의 카드덱)
        if check_run_triplet(p1):
            winner = 1
            break

        #i + 1 번째 카드가 p2의 카드 >> p2가 카드덱을 만들기
        p2[numbers[i+1]] += 1
        # check_run_triplet(p2의 카드덱)

        if check_run_triplet(p2):
            winner = 2
            break

    print('#{} {}'.format(tc,winner))



