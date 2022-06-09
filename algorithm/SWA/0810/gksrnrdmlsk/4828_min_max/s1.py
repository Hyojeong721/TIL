import sys
sys.stdin = open('input.txt')

case = int(input()) # 몇 번의 테스트 케이스가 있을지 입력받습니다.

for i in range(case):
    numbers = int(input()) # 몇 개의 숫자가 들어올지 입력받습니다.
    lst = list(map(int, input().split())) # 입력받은 숫자로 리스트를 만듭니다.
    temp_min = lst[0] # 현재까지 최솟값을 저장합니다.
    temp_max = lst[0]
    for j in lst:
        if j > temp_max: # 기존의 최댓값보다 크면 최댓값을 업데이트합니다.
            temp_max = j

        elif j < temp_min:
            temp_min = j

    print('#%s'%(i+1) ,temp_max - temp_min)

