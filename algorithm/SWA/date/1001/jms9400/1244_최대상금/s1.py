import sys
sys.stdin = open('input.txt')

T = int(input())


def change(lst, N):
    n = len(lst)
    if N == 0:
        return lst
    if n <= 2:  # 만약 N이 남아있는데 바꿀자리가 두자리라면 남은 N이 짝수인지 홀수인지 확인
        if N % 2 == 0:
            return lst
        else:
            lst[0], lst[1] = lst[1], lst[0]
            return lst

    temp = []
    Ma = 0  # Ma는 최댓값 인덱스
    for i in range(n):  # 선택정렬
        if lst[i] > lst[Ma]:
            Ma = i
            if temp:
                temp = []
        elif lst[i] == lst[Ma] and i != 0:
            temp.append(i)

    if temp:  # max인 숫자가 여러개 있다면
        new_lst = sorted(lst, reverse=True)
        if lst == new_lst:  # 같은 숫자끼리 바꿔주는 게 젤 큰 수 이면
            return lst
        else:
            lst[0], lst[Ma] = lst[Ma], lst[0]
            return [lst[0]] + change(lst[1:], N)
    else:
        if Ma == 0:
            return [lst[0]] + change(lst[1:], N)
        else:
            lst[0], lst[Ma] = lst[Ma], lst[0]
            return [lst[0]] + change(lst[1:], N-1)


for tc in range(1, T+1):
    numbers, N = input().split()
    N = int(N)
    numbers = list(map(int, numbers))
    print('#{} {}'.format(tc, ''.join(map(str, change(numbers, N)))))

