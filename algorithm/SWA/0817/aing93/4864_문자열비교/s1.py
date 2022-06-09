import sys
sys.stdin = open("input.txt")

T = int(input())
# 첫 포문에 인풋을 받고 result를 0으로
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0
    #두번째 포문은 레인지를 N-M+1
    for i in range(len(str2)-len(str1)+1):
        # 이프문에 str2에서 i에서 i+str1의 길이만큼 슬라이싱.
        # 그 값이 str1이랑 같으면 result = 1로 하고 break 해서 나가기.
        if str2[i:i+len(str1)] == str1:
            result = 1
            break

    print('#{} {}'.format(tc, result))