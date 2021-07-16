# command

> git 기본 명령어 관리

##### log

- 커밋의 히스토리를 보여주는 명령어

```bash
git log
```





### 관리(로컬)

##### add

- working directory에서 staging area에 파일을 업로드 하는 명령어
  - `.`현재 폴더, 하위 폴더, 하위 파일 모두 

```bash
git add <file name>
# git add . 
```



##### commit

- ​	staging area에 올라온 파일들을 하나의 커밋으로 만들어주는 (스냅샷 찍는) 명령어

```bash
git commit -m "commit message"
```



### 관리(원격)

##### remoate add

- 원격 저장소 주소를 로컬에 저장하는 명령어
  - nickname에는 일반적으로 `origin` 

```bash
git remote add <nickname> <url>
```



##### push

- 원격 저장소로 로컬의 커밋기록을 업로드하는 명령어

```bash
git push <nickname> <branch name>
```

