import sys
sys.stdin = open('input.txt')

number = int(input()) # 몇 번의 테스트 케이스가 있을지 입력받습니다.

for i in range(number): # 테스트 케이스 개수만큼 반복합니다.
    size = int(input()) # 방의 크기를 입력받습니다.
    lst = list(map(int, input().split())) # 상자 분포 리스트를 입력받습니다.
    temp_idx = 0 # 낙차가 가장 큰 상자의 인덱스를 위해 지정합니다.
    temp_value = 0 # 최대 낙차를 계산하기 위해 지정합니다.
    for idx, value in enumerate(lst[:-1]): # 인덱스와 크기가 모두 필요하므로 enumerate를 이용합니다.
        count = 0 # 낙차를 계산합니다.
        for j in range(idx + 1,size):
            if value > lst[j]:
                count += 1
            else:
                pass
        if count > temp_value: # 해당 줄의 낙차가 현재까지 가장 클 경우 그를 저장합니다.
            temp_value = count
            temp_idx = idx

    print('%s번째 상자가 %s로 낙차가 가장 큽니다.' %(temp_idx+1, temp_value))


