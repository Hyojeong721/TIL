
## 개수를 모르는 입력값 처리하는 방법

이 문제와 같이 테스트 케이스의 개수가 정해지지 않은 경우,

테스트 케이스의 개수만큼 반복문을 도는 방법으로는 정해진 데이터를 모두 처리할 수 없다.

이러한 경우를 처리하는 한 가지 방법으로는 

`try ~ catch`문과 `EOFError` 에러를 활용한 예외 처리가 있다.

```bash
exception EOFError

input() 함수가 데이터를 읽지 못한 상태에서 EOF (end-of-file) 조건을 만날 때 발생합니다.

(출처: https://docs.python.org/ko/3/library/exceptions.html)
```

위의 에러를 활용하여, 무한루프를 통해 입력값을 받다가 파일의 끝에 다다르면 무한루프를 빠져나오게 만들 수 있다.

```python
while True:
    try:
        tc, route_count = map(int, input().split())
    except EOFError:
        break
```
