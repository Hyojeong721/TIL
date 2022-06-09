import sys
sys.stdin = open('input.txt')

# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성
# 대소문자 구분 x

string = input()
alpa = {}

for i in string:
    temp = ord(i)
    # 대문자를 소문자 숫자로 저장하기
    if temp > 90:
        temp = ord(i)-32
    # 반복횟수 저장
    if chr(temp) in alpa:
        alpa[chr(temp)] += 1
    else:
        alpa[chr(temp)] = 1

# 최대 반복인 값 찾기위해 오름차순 정렬
values = list(alpa.values())
values.sort()

# # 맥스값이 동일한 글자가 2개이상이면
if len(values) > 1 and values[-1] == values[-2]:
    print('?')
else:
    # key와 value 자리 바꾸기
    reverse_alpa = {v:k for k, v in alpa.items()}
    # 대문자로 출력
    print(reverse_alpa)
    print(reverse_alpa[values[-1]])

