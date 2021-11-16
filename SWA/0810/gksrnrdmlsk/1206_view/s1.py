import sys
sys.stdin = open('input.txt')

def my_max(*args): # max 썼다는 비판을 방어하기 위해
    result = args[0]
    for arg in args:
        if arg > result:
            result = arg
    return result


T = 10 # 10번의 테스트 케이스가 주어진다.
for tc in range(1, T + 1):
    width = int(input())
    lst = list(map(int, input().split()))
    count = 0
    try:
        for i in range(2, width - 2):
            neighbor = my_max(lst[i - 2], lst[i - 1], lst[i + 1], lst[i + 2])
            if lst[i] > neighbor: # 양 옆 네 개의 빌딩과 높이 비교
                count += (lst[i] - neighbor)
        print('#{} {}'.format(tc, count))
    except:
        print('#{} {}'.format(tc, 0))
