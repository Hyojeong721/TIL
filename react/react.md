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





### State

```js
import { useState } from 'react';

const [num, setNum] = userState(1);

```

1은 초기값으로 받는 거

배열 -> 첫번째 요소가 바로 state, 두번째 요소가 이 state를 바꾸는 setter함수



#### 참조형 state

 ```js
 const [game, setGame] = userState([]);
 
 const handleRollClick = () => {
     const nextNum = random(6);
     game.push(nextNum);
     setGame(game); // 이러면 state가 제대로 변경되지 않는다. 이유는 state는 배열주솟값을 참조하기 때문
     setGame([...game, nextNum]); //이렇게 새로운 참조형 값을 만들어 변경해야한다. 
 }
 ```



####  state lifting 

자식 컴포넌트의 state를 부모로 올리는 거



### F2

F2누르고 app -> apple로 변경하면 그 파일에 있는 모든 app 이름이 apple로 변경



### 스타일 적용하기

index.css 파일을 만들어서

```js
. body {
    background-color: black,
}
```

 ```js
 import './index.css';
 
 // head에 스타일로 적용된다. 
 ```







### 명령어

- 프로젝트 생성하기

  ```
  npm init react-app .
  ```

- 개발 모드 실행하기

  ```
  npm start 
  npm run start
  ```

- 실행중인 서버 종료하기

  ctrl + c

- 개발된 프로젝트 빌드하기

  ```
  npm run build
  ```

- 빌드한 것 로컬에서 실행하기

  ```
  npx serve build
  ```

  

### 웹브라우저가 react를 알아먹는 과정

jsx로 만들어진 파일 

-> Transpiling(트랜스 파일링)

js로 변환됌

-> Bundling(번들링)

하나의 묶음 js파일 생성됌

-> 브라우저가 알아먹음! 
