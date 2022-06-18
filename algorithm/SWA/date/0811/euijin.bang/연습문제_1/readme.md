#### 문제포인트 
- 이차원 리스트를 초기화할 수 있는가
- 델타검색을 돌 수 있는가
- 델타검색을 돌 때, 이차원 리스트의 가장자리 부분을 처리할 수 있는가
- 절대값을 계산할 수 있는가

#### 오류
- `index out of range` 발생

#### 원인
- 델타검색시 이차원 리스트의 가장자리 범위를 고려하지 못함

#### 해결
- 직접 써보면서 확인하여 수정, if 문으로 범위를 제한
```
   for i in range(N):
        for j in range(N):
            for k in range(4):
                if (i + del_i[k] >= 0 and i + del_i[k] < N) and (j + del_j[k] >= 0 and j + del_j[k] < N):
                    #(arr[i + del_i[k]][j + del_j[k]])