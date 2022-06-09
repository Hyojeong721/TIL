# 해당 배열의 모든 부분집합을 구하기

# 전체 배열
# arr = ['하나', '둘', '셋']
arr = [1, 2, 3]

# 배열의 길이 => 재귀함수의 종료조건에 활용
N = len(arr)

# 어떤걸 골랐는지 체크하는 배열
# 내가 해당 원소를 뽑았는지 체크하기 위한 배열
sel = [0] * N

def powerset(idx):
    if idx == N:
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return
    # sel 배열의 index 자리를 1로 바꾼다 => 해당 원소를 뽑았다!
    sel[idx] = 1
    # 다음 경우의 수로 진입
    powerset(idx+1)

    # sel 배열의 index 자리를 0으로 바꾼다 => 해당 원소를 뽑지 않는 경우!
    sel[idx] = 0
    # 다음 경우의 수로 진입
    powerset(idx+1)


powerset(0)


# def powerset(idx, ):
#     if idx == N:
#         print(sel)
#         return
#
#     # sel 배열의 index 자리를 1로 바꾼다 => 해당 원소를 뽑았다!
#     sel[idx] = 1
#     # 다음 경우의 수로 진입
#     powerset(idx+1)
#
#     # sel 배열의 index 자리를 0으로 바꾼다 => 해당 원소를 뽑지 않는 경우!
#     sel[idx] = 0
#     # 다음 경우의 수로 진입
#     powerset(idx+1)