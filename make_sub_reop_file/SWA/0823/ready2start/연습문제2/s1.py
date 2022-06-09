# 전체 배열
arr = [1, 2, 3]
# 배열의 길이 => 재귀함수의 마지막 위치를 확인할 때 사용
N = len(arr)
# 해당 원소를 뽑았는지 체크하기 위한 배열
selected = [0] * N


def powerset(idx):
    if idx == N:
        for i in range(N):
            if selected[i]:
                print(arr[i], end=" ")
        print()
        return

    # selected[idx]를 1로 바꾼다 => 해당 원소를 뽑은 경우
    selected[idx] = 1
    # 다음 경우의 수로 진입한다.
    powerset(idx + 1)

    # selected[idx]를 0으로 바꾼다 => 해당 원소를 뽑지 않은 경우
    selected[idx] = 0
    # 다음 경우의 수로 진입한다.
    powerset(idx + 1)


powerset(0)

