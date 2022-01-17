# GIT



### git commit에 관한 주의사항

1. 처음으로 커밋하기 전에는 사용자의 이름과 이메일 주소를 설정

````
git config user.name <username>
git config user.email <useremail>
````

2. 커밋할 파일을 git add로 지정해주기

```
git add . (or 파일명)
```

3. 커밋메시지 남기기 

```
git commit -m "메시지"
```



<br>

### 3가지 종류의 작업 영역

#### working directory (working tree)

작업을 하는 프로젝트 디렉토리를 말한다.

=> git add <파일>

#### staging area (index)

git add를 한 파일들이 존재하는 영역

커밋하게 되면 staging area에 있는 파일들만 커밋에 반영된다.

=> git commit -m "v1"

#### repository

working directory의 변경 이력들이 저장되어 있는 영역



<br>

### staging area에서 파일 제거! (git add 한거 빼기)

``` 
git reset <파일명>
```

주의! 그래도 변경된 상태로 working directory에 남아있다는 거~!!

<br>



### 레포지토리

- 깃허브의 레포지토리 = 원격 레포지토리 = 리모트 레포지토리

  <-> 내 컴퓨터의 레포지토리 = 로컬 레포지토리

<br>

### 리모트 레포지토리를 만드는 이유

1. 안전성 
2. 협업가능

<br>

### git push

로컬 -> 리모트

<br>

### git pull 

로컬 <- 리모트

<br>

### git clone

깃허브 프로젝트의 레포지토리를 그대로 복제



### 커밋히스토리

```
git log
git log --pretty==oneline // 더 깔끔하게 보임
```

커밋정보들이 나타남

커밋의 더 자세한 정보를 보려면

```
git show 커밋아이디(앞에 4자리 정도만 쳐도 나옴)
```

<br>



### 커밋메시지

```
git commit
```

하면 commit을 쓸 수 있는 텍스트 에디터가 나옴

거기에서 i(insert) 누르고 작성후 esc 누르고 ':wq' 누르고 나오면 완성~



- 커밋메시지 작성 가이드라인

  - 제목과 상세설명 사이에는 한줄을 비우기

  - 커밋메시지 제목뒤에 온점 x

  - 커밋메시지 제목의 첫번째 알파벳은 대문자로 작성

  - 제목은 명령조로 작성

  - 상세내용에는

    - 왜 커밋함?
    - 어떤 문제있었음?
    - 적용한 해결책이 어떤 효과를 가짐?

    



#### 커밋 최근 메시지 수정

``` 
git commit --amend
```

최신 커밋을 수정해서 다시 새로운 커밋으로 만들기

<br>

