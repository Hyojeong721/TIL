# 1028_Flatten

```python
import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    dump = int(input())
    case = list(map(int,input().split()))
    for dump in range(1, dump+2):******************#1*************
        # 최대 최소 구하기
        my_max = case[0]
        my_min = case[0]
        my_max_index = 0
        my_min_index = 0

        for i in range(len(case)):
            if my_max <= case[i]:
                my_max = case[i]
                my_max_index = i

            if my_min >= case[i]:
                my_min = case[i]
                my_min_index = i
        # 최고높이 -1 최저높이 +1 평탄화
        case[my_max_index] -= 1
        case[my_min_index] += 1

        #출력 값
        result = my_max - my_min
        if dump == dump + 1 or 0 <= result <= 1:
            print(result)

    print('#{} {}'.format(tc, result))
```

- #1 - range의 범위

  이 부분 처음에 고민없이 (1, dump+1) 로 작성했다.

  그런데 범위를 dump+1로 하면 6번째 케이스에서 출력값이 1 적게 나온다.

  (1, dump+1) => 주어진 덤프횟수만큼 진행된다. 

