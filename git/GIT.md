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

#### 두 커밋 사이의 변화 알아보기

```
git diff <commit key1(앞에 4자리만)> <commit key2>
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

### HEAD

어떤 커밋 하나를 가리키고 가리킨 커밋이 working directory 구성됌

보통 가장 최근에 한 커밋을 가리킴 

#### 과거의 커밋을 가리키게 = git reset

```
git reset --hard <commit id>
```

그럼 working directory의 내용도 과거 커밋의 모습으로 돌아가게 된다.

<br>

#### 옵션

- --soft : repository는 가리키지만 working directory, staging area 안바뀜
- --mixed : staging은 바뀌지만 working은 안바뀜
- --hard :  working, staging 바뀜



### 기타

- git config aliiias.[별명] [커맨드] : 길이가 긴 커맨드에 별명을 붙여서 이후애 별명으로 해당 커맨드 실행
- git tag [태그이름] [커밋 아이디] : 특정 커밋에 태그를 붙임



## 브랜치 branch

하나의 코드 관리 흐름

#### 브랜치 생성

```
git branch [브랜치이름]
```

#### 브랜치 이동

```
git checkout [브랜치이름]
```

#### 브랜치 조회

```
git branch
```

,현재 있는 브랜치에 * 표시

#### 브랜치 삭제

```
git branch -d [브랜치이름]
```

#### 브랜치 생성 + 이동

```
git checkout -b [브랜치이름]
```

<br>

### branch merge

```
git merge 합치고싶은브랜치이름
```

커밋메시지 창 뜨면 :wq

#### conflict

- 머지를 하다가 충돌이 발생했다!

  1. 컨플릭트가 발생한 파일을 연다
  2. 원하는대로 수정하고
  3. 커밋한다.

   or

  머지 취소!

  ```
  git merge --abort
  ```

   

### git fetch

리모트 레포지토리에 있는 브랜치의 내용을 일단 가져와서 살펴본 후에 머지하고 싶을 때 사용

혹은

리모트 레포지토리에 있는 브랜치의 내용과 내가 작성한 코드를 비교해서 검토해야할 때

git fetch -> git diff



- git pull은 리모트레포지토리 브랜치내용을 가져와서 머지까지 해주는 것.

 => git pull = git fetch + merge

premium -> origin/premium

리모트내용이 로컬로 들어왔다는 것 로컬은 origin/premium이라고 나타난다.



- 리모트 레포지토리의 브랜치에 문제가 있을 때 
  - 잘못된 코드 추가한 개발자에게 코드 수정 요청 후 다시 리모트 레포지토리에 올려달라고 하기
  - or
  - 잘못된 부분을 알아서 해결하고 다시 git push하기

<br>

### git blame

이코드는 누가 작성했을까 하는 

``` 
git blame 파일명
```

<br>

### git revert

```
git revert [커밋 아이디]
```

4번째 커밋상태로 바꾸고 싶을때, (리모트 레포지토리에도 푸쉬를 해버린상태에서)

reset안되고 revert해야한다. 

reset하면 로컬은 5번째에서 4번째로 가지만 리모트는 5번째에 있기때문에

그다음 푸쉬가 안된다.

<br>

#### 여러개 커밋을 수정하고 싶을때

```
git revert [커밋아이디]..[커밋아이디]
```

근데 앞에 커밋아이디는 포함안된다.

