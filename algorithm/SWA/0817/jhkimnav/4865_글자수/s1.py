import sys
sys.stdin = open('input.txt')


T = int(input())

for TC in range(1, T+1):
    answer = 0
    # st1에 포함된 각각의 글자들이 str2에 몇 개씩 들어있는지 찾고
    # 가장 많은 글자 수 출력
    str1 = input()
    str2 = input()
    dic = {}
    for c in str1:
        dic[c] = 0

    for char in str2:
        if char in dic:
            dic[char] += 1
    answer = max(dic.values())
    print('#{} {}'.format(TC, answer))