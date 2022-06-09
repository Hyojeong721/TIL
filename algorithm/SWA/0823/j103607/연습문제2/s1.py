# 전체 배열
arr = ['하나', '둘', '셋']
# 배열의 길이 => 재귀함수의 마지막 위치를 확인할 떄 활용
N = len(arr)
# 해당 원소를 뽑았는지 체크하기 위한 배열
sel = [0] * N

def powerset(idx):
    if idx == N:
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return

    # sel배열의 index자리를 1로 바꾼다 => 해당 원소를 뽑았다!
    sel[idx] = 1
    # 다음 경우의 수로 진입
    powerset(idx+1)

    # sel배열의 index자리를 0으로 바꾼다 => 해당 원소를 뽑지 않은 경우
    sel[idx] = 0
    # 다음 경우의 수로 진입
    powerset(idx+1)


powerset(0)