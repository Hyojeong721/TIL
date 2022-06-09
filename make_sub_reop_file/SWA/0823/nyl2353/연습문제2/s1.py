# 전체 배열
arr = ['하나', '둘', '셋']
# 배열의 길이 => 재귀함수의 마지막 위치를 확인할 때 활용
N = len(arr)
# 내가 해당 원소를 뽑았는지 체크하기 위한 배열
sel = [0] * N

def powerset(idx):
    if idx == N:
        # 선택한 원소들의 index 출력
        # print(sel)
        # 선택한 원소들을 출력
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return

    # sel 배열의 index 자리를 1로 바꾼다 => 해당 원소를 뽑았다!
    sel[idx] = 1
    # 다음 경우의 수로 진입
    powerset(idx + 1)

    # sel 배열의 index 자리를 0으로 바꾼다 => 해당 원소를 뽑지 않는 경우!
    sel[idx] = 0
    # 다음 경우의 수로 진입
    powerset(idx + 1)


powerset(0)