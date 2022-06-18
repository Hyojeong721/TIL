arr = ['하나', '둘', '셋']

N = len(arr) # 배열의 길이 => 재귀함수의 마지막 위치를 확인할 때 활용
sel = [0] * N # 내가 해당 원소를 뽑았는지 체크하기 위한 배열. 즉, 예전의 visited와 같은 역할! (select의 약자)

def powerset(idx):
    if idx == N:
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return # 함수 끝내주려고!

    # sel 배열의 index 자리를 1로 바꾼다 => 해당 원소를 뽑았다!
    sel[idx] = 1
    # 다음 경우의 수로 진입
    powerset(idx + 1)

    # sel 배열의 index 자리를 0으로 바꾼다 => 해당 원소를 뽑지 않는 경우!
    sel[idx] = 0
    powerset(idx + 1)

powerset(0)