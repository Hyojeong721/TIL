import sys
sys.stdin = open("input.txt")
T = int(input())


for i in range(1, T+1):
    get_date = input()
    # print(get_date) 입력 데이터 받아옴
    year = get_date[0:4]
    month = int(get_date[4:6])
    date = int(get_date[6:8])
    if 1 <= month <= 12 and 1 <= date <= 31:
        if month == 2 and 29 <= date:
            print('#{} -1'.format(i))
        elif month in [4, 6, 9, 11] and date == 31:
            print('#{} -1'.format(i))
        else:
            print('#{} {}/{}/{}'.format(i, get_date[0:4], get_date[4:6], get_date[6:8]))
    else:
        print('#{} -1'.format(i))
