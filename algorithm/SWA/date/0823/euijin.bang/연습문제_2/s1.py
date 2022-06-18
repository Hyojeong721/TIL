# 재귀 호출로 1이 있고 없고를 나누고, 다시 2가 있는경우 없는 경우.... 트리 구조로 나눔

# 전체 배열
arr = ['하나', '둘', '셋']
# 배열의 길이 => 재귀함수의 마지막 위치를 확인 할 때 활용
N = len(arr)
# 내가 해당 원소를 뽑았는지 체크하기 위한 배열
sel = [0] * N # select : 각 노드를 방문했는지 확인하기 위한 리스트


def powerset(idx):
    if idx == N:
        for i in range(N):
            if sel[i] == 1:
                print(arr[i], end=' ')
        print()
        return

    # sel 배열의 index 자리를 1로 바꾼다 => 해당 원소를 뽑았다!
    sel[idx] = 1 # 1이 있을 때 파워셋을 호출
    # 다음 경우의 수로 진
    powerset(idx+1) # 쭉 증가하는데 우리는 0, 1, 2 인덱스까지만 필요, 3일때 종료


    # sel 배열의 index 자리를 0으로 바꾼다 => 해당 원소를 뽑지 않는 경우!
    sel[idx] = 0 # 1이 없을 때 파워셋을 호출
    # 다음 경우의 수로 진입
    powerset(idx+1)


powerset(0) # 0 번 인덱스 기준으로 출력