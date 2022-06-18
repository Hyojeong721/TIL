#### 문제

```python
sys.stdin = open("input.txt")
```

`input.txt` 파일을 위와 같이 열었더니 아래와 같은 오류가 발생했다.

```bash
UnicodeDecodeError: 'cp949' codec can't decode byte 0xec...
```

찾아보니 cp949 코덱으로 인코딩된 파일을 읽을 때 위와 같은 오류가 발생한다고 한다.



#### 해결

1. 인코딩 방식을 'UTF-8'로 명시한다.

```python
sys.stdin = open("input.txt", encoding="UTF-8")
```

2. 텍스트 파일을 다른 이름으로 저장한다. 저장할 때 인코딩 방식을 **ANSI**로 바꾼다.

