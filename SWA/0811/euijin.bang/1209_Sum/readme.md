#### 문제포인트 
- 행우선순회, 열우선순회, 대각선 순회
- 리스트 `append`, `extend` 활용

#### 오류
- `index out of range` 발생

#### 원인
- 대각선 순회에서 범위설정 오류

#### 해결
- 직접 써보면서 확인하여 수정
```
    for i in range(100):
        total_left = arr[i][i]
    for i in range(100):
        total_right += arr[i][100 - i - 1]
```