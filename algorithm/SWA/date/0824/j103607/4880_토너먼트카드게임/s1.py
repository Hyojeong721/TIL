import sys
sys.stdin = open('input.txt')

'''
아직 덜했음...
'''

# 게임 진행되는 함수(승자 정하는 함수)
# 1: 가위 2: 바위 3: 보
def game(a, b):

    if (a == 1 and b == 3) or (a == 1 and b == 1):
        return 1
    elif (a == 2 and b == 1) or (a == 2 and b == 2):
        return 1
    elif (a == 3 and b == 2) or (a == 3 and b == 3):
        return 1
    else:
        return 0


# 학생 두 그룹으로 나누는 함수
def group(student_list):
    if len(student_list) == 1:
        return student_list[0]
    elif len(student_list) % 2:
        group1 = student_list[0:len(student_list)//2+1]
        group2 = student_list[len(student_list)//2+1:]
    elif len(student_list) % 2 == 1:
        group1 = student_list[0:len(student_list)//2]
        group2 = student_list[len(student_list)//2:]

    # 나눠진 그룹에서 계속 그룹 나누기
    x = group(group1)
    y = group(group2)

    if game(x[0], y[0]) == 1:
        return x
    else:
        return y

T = int(input())
for tc in range(1, T+1):

    # 학생 수
    N = int(input())
    # 각 학생이 고른 카드 번호 리스트
    num_list = list(map(int, input().split()))
    num_list_idx = [(j, i+1) for i, j in enumerate(num_list)]

    result = group(num_list_idx)

print(result)