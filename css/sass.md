# Sass 

### Sass란?

> css를 프로그래밍 언어스럽게 작성가능한 프리프로세스, css문법을 다채롭게 하는 거~

그런데!!

브라우저는 sass문법을 모름~

sass 작성파일 -> css 파일로 다시 컴파일 필요!

그걸 **node-sass 라이브러리**가 해줌



### 설치

```
npm install node-sass
```



### 사용법

1. sass 파일 작성 (ex- detail.sass 생성 후, 작성)

2. css적용할 js파일에 import (ex - detail.js에서 import './detail.sass')

   

### scss 문법

1. **변수**에 데이터를 저장해서 쓰자

   - 변수만드는 법 : 

     - ```
       $메인칼라 : #89200;
       ```

2. **@import** 파일 경로

   - 자주 쓰는 문법인데 계속 작성하기 어려우니까 
     reset.scss에 적어놓고 그걸 다른 .scss에서 import해서 써!

   - ```
     # reset.scss
     body {
     margin :0;
     }
     div {
     	box-sizing: border-box;
     }
     ```

   - 그리고 detail.scss에서 @'./reset.scss' 하면 적용됌

   

3. 셀렉터 대신 쓰는 **nesting 문법**

   - 이런식으로 길어지는 보기싫은 경우

     ```
     div.container h4 {
     	color : blue;
     }
     div.container p {
     	color : blue;
     }
     ```

   - 이걸 사스문법으로 바꾸면

   - ```
     div.container {
     	h4 {
     		color : blue;
     	}
     }
     div.container {
     	p{
     		color : blue;
     	}
     }
     ```

4. **@extend** // **@mixin / @include**

   - ```
     .my-alert {
     	background: #eeeee;
     	padding: 20px;
     	border-radius:5px;
     	max-width: 500px;
     	width:100%;
     	margin:auto;
     }
     .my-alert p {
     	margin-bottom: 0l
     }
     ```

   - 비슷한 걸 여러개로 만들고 싶다

     - 방법1. my-alert2 만들어서 기존 코드 복붙

     - 방법2. @extend

       - ```
         .my-alert2 {
         	@extend .my-alert;  # my-alert의 모든 속성 가져옴(복붙)
         	background: #ffe591  # 다 똑같고 색상만 달라짐
         }
         ```

     - 방법3. @mixin / @include

       - ```
         @mixn 함수 {
         	background: #eeeee;
         	padding: 20px;
         	border-radius:5px;
         	max-width: 500px;
         	width:100%;
         	margin:auto;
         }
         
         .my-alert {
         	@include 함수()
         }
         .my-alert2 {
         	@include 함수();
         	background: #ffe591;
         }
         ```