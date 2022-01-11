# react 학습



## react 프로젝트 생성하기

```
npm init react-app <폴더이름>
npm init react-app .  -> 폴더들어가 있는 상태에서 
```

<br>

#### 프로젝트 실행

```
npm run start
```



App..j수정



- component : react 개발의 가장 기본적인 단위

<br>

### public > index.html

- 웹브라우저에서 제일 먼저 실행되는 파일

  <br>

### src > index.js

- index.html이 열리고 나서 실행되는 파일

- react코드들 중에서 갖아 먼저 실행되는 곳

  <br>

### jsx

javacsript에서  html  문법을 사용할 수 있는 확장 문법

- 속성명은 카멜 케이스로 작성
  - 단 예외적으로 html에서 비표준 속성을 다룰 때 활용하는 data-*속성은 카멜케이스아님
- 자바스크립트 예약어와 같은 속성명은 사용할 수 없다.
  - className 
  - htmlFor

<br>



### 프래그먼트

jsx에서는 반드시 하나의 태그로 감싸줘야 하는데 이럴때 사용한다.

불필요한 div태그를 대체할 수 있다. 

```js
ReactDOM.render(
	<div> -> <Fragment> -> <>(축약형)
    	<p>ddddksudsk</p>
    	<p>hi</p>
    </div> -> </Fragment> -> </>
)
```

<br> 

### jsx에서 자바스크립트 사용하기

{} 중괄호로 감싸기! 

```js
const product = "win"

ReactDOM.render(
	<>
    	<p> 나의 아이템 {product} </p>
    </>
)
```

