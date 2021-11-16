### 문제 포인트
- 1차원 리스트를 인덱스접근 아닌 다른 방식으로 구현할 수 있는가
- 문제의 조건을 파악하여 코드를 구현할 수 있는가
- 다양한 반복문과 조건문, 제어문을 사용할 수 있는

### 어려웠던 점
- 다양한 변수파악, 문제에서 묻는 바를 구현하기 어려웠다.
- 문제 접근방법 어려웠다. 

### 해결
- 현재 위치와 충전 횟수라는 변수를 사용
- 현재 위치에서 이동가능 거리를 더하면서 이동하는 방식
- 충전기를 만나면 충전하고, 못만나면 이동거리를 줄여가며 반복하는 방식
- `for else` 구문 사용
```
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()
```