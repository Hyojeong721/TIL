import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # str1 에서 중복 제거
    str1 = set(input())
    str2 = input()

    # 최대 수를 계속 업데이트
    maximum = 0
    for _ in range(len(str1)):
        finding = str1.pop()
        cnt = 0
        for char in str2:
            if char == finding:
                cnt += 1
        if maximum < cnt:
            maximum = cnt

    print('#{0} {1}'.format(tc, maximum))


'''

str 에 list set 안하고, 바로 set 씌워도 된다.

'''