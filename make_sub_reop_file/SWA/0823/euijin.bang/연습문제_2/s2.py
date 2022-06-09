# 부분집합의 합이 10인 부분집합을 출력

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(data)
sel = [0] * N

def powerset(idx):
    # 아직 부분집합을 다 찾지 못한 경우
    if idx < N:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)
    # 전체 길이를 다 확인한 경우(바닥에 도착한 순간 데이터를 합)
    else:
        total = 0
        for i in range(N):
            if sel[i] == 1:
                total += data[i]

        if total == 10:
            for i in range(N):
                if sel[i] == 1: # 돌면서 1인 것만 골라서 출
                    print(data[i], end=' ')
            print()
        return

powerset(0)