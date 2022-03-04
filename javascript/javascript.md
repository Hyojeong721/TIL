# Web API

### web(world wide web)

연결망 체계

수많은 웹페이지를 돌아다닌다.

무수히 많은 웹페이지들이 연결되어 있다.

<br>

### HTML = hyper text markup language

<br>

### URL = Uniform Resource Locator

웹에 존재하는 특정 데이터를 나타내는 문자열

url -> Scheme(https) + host + path + query

Scheme = 프로토콜의 이름

: 요청과 응답의 형식을 정해줌 요청할때도 응답할때도 https 프로토콜을 준수하면서 오고간다.

<br>

### JSON = JavaScript Object Notation

- JSON의 경우 js와 달리 프로퍼티의 이름에 반드시 큰따옴표를 붙여줘야 한다.
- json은 무조건 큰따옴표 js는 작은따옴표도 가능
- json은 주석 추가 금지
- 응답받는 타입은 string타입임 -> **JSON.parse** 사용하면 자바스크립트 객체로 바꿔준다.

<br>

### Request

#### 종류

- GET 조회

- POST 추가

- PUT 수정

- DELETE 삭제

- 기타

  - PATCH : 기존데이터를 수정할때 사용하는 메소드
    - PUT과 다른 점은 새 데이터로 기존 데이터의 일부를 수정하는것
    - PUT은 기존데이터를 아예 새롱누 데이터로 덮어씀으로써 수정

  - HEAD : GET 메소드와 동일함, GET과 다른점은 리스폰스에서 딱 헤드만 받음
    - 용량이 큰 파일을 정보만 필요할때 헤드만 받는경우에 사용가능

#### 구성

GET, DELETE => HEAD

POST, PUT => HEAD-BODY

#### POST 추가 (옵션객체에 method, body 추가!!)

```js
fetch('url', {
    method:'POST'
    body: JSON.stringify(newMember),
})
```

**stringify** => jv객체에서 json 형식을 바꿔주는 것.

Json -> javascript : parse

Json <- javascript : stringify

#### PUT 수정

```js
fetch('url/수정할객체의id', {
    method:'PUT'
    body: JSON.stringify(Member),
})
```

#### DELETE 삭제

```JS
fetch('url/삭제할객체의id', {
    method:'DELETE'
})
```

<br>

### REST API

web API를 설계할 때, 준수하기 위해 노력하는 일종의 가이드 라인

REST architecture에 부합하는 API를 의미한다.

#### REST architecture

<br>

### response

HEAD : RESPONSE에 대한 부가정보

BODY : 실제 데이터를 담는 부분 JSON 데이터

#### HEAD에 있는 header

- Status Code 

  - 1xx
  - 2xx
  - 3xx
  - 4xx 
  - 5xx

- Content-Type

  : 리스폰스의 바디에 들어있는 데이터가 어떤 타입인지를 나타낸다.

  #### 헤더를 설정하고 싶을때

  ```js
  fetch('url', {
      method:'POST',
      header: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(newMember),
  })
  ```

  #### type

  - JSON

  - XML

  - application/x-www-form-urlencoded

    : form태그만으로 리퀘스트를 보내는 방식에서 이 타입에 데이터를 바디에 담아 보냄

    ##### 방법

    -form 태그로 보내면 기본이 이거라서 딱히 지정할 필요 없음

    ```
    id=6&name=json&age=34
    ```

  - multipart/form-data

    : 여러 종류의 데이터를 하나로 합친 데이터를 의미하는 타입

    : 예를 들어, 게시글에서 이미지파일과 게시글등을 업로드할때

    ##### 방법

    1. html 코드로 하는 방법

       ```html
       <form method="post" enctype="multipart/form-data">
       ```

       

    2. 자바스크립트 코드로 하는 방법

       ```javascript
       const formData = new FormData();
       formData.append('email', email.value);
       formData.append('profile', image.files[0], "me.png");
       
       
       fetch('url', {
           method:'POST',
           body: formData,
       })
       ```

<br>

### fetch

웹 브라우저에서 서버로 request를 보내고 

서버에서 웹브라우저로 response 받을수 있다.

<br>

### Ajax 통신 vs Ajax 통신이 아닌것

Ajax 통신이 아닌것

```html
<a href="url">메인화면</a>
```

Ajax 통신

```javascript
fetch('url')
	.then((response) => response.text());
	.then((result) => console.log(result))
```

<br>

<hr>

# 통신을 위한 javascript

### 동기 vs 비동기 실행

- 비동기 실행 : 작업이 끝나기를 기다리지않고 코드 작성순대로 계속 진행되는것
- 동기 실행 : 코드작성에서 한줄의 코드 실행이 종료된 후 다음 줄의 코드가 진행되는 것

<br>

#### 비동기 실행 함수

- fetch
- setTimeout : 특정 함수의 실행을 원하는 시간만큼 뒤로 미루기 위해 사용하는 함수



### DOM

- 요소노드
- 텍스트노드



#### 요소 노드에 대한 이동 프로퍼티

- 자식요소노드
  - element.children
  - element.firstElementChild
  - element.lastElementChild
- 부모요소노드
  - element.parentElement
- 형제요소노드
  - element.previousElementSibling
  - element.nextElementSibling

#### 모든 노드에 대한 이동 프로퍼티는

 요소노드이름에서 element라는 단어만 빼면됌.



#### 요소 노드의 프로퍼티

- tag.textContent : 태그를 제외하고 텍스트만 가져옴 / innerHTML과 동일하게 내부의 값을 새로운 값으로 교체 / 특수문자도 텍스트 처리

- tag.outerHTML : 요소 노드 내부의 전체 HTML 코드를 문자열로 리턴 -> 새로운값 할당하면 요소 자체가 교체되어 버리므로 주의!

- tag.innerHTML : 요소 노드 내부의 HTML 코드를 문자열로 리턴 / 내부HTML자체 수정때 활용

  새로 추가하면 새로운걸로 교체하는 방식 

<br>

#### 요소 노드 추가하기 (기본 내용을 보존한 상태로 ) / 이동하기

- node.prepend
- node.append
- node.before
- node.after

<br>

#### 요소 노드 삭제하기

node.remove()

<br>

### HTML 속성을 다루는 메소드

#### 속성에 접근하기

element.getAttribute('속성')

#### 속성 추가 수정하기

element.setAttribute('속성', '값')

#### 속성 제거하기

element.removeAttribute('속성')

<hr>

# event

#### addEventListener(event, handler)

#### removeEventListener(event, handler)

handler부분에는 이름만!! ()넣지마세요~

<br>

## fetch 

### promise = fetch함수가 리턴하는객체 

자바스크립트 비동기 실행에 있어서 아주 핵심적인 문법

##### 작업 상태 정보를 갖는다.

- pending : 작업진행중

- fulfilled : 작업성공 -> promise에 작업성공결과(response)도 갖는다 
- rejected : 작업실패 -> promise에 작업실패정보도 갖는다.

<br>

##### promise객체가 fulfilled상태일때 사용하는 메소드 => then

- then : fulfilled 상태가 됐을때, 실행될 콜백을 등록하는 메소드

  콜백성공했을때 결과를 받는다. 

  return => promise객체 / 일반객체 모두 가능

**Promise Chaining** = then메소드 연결연파람결연결연결=> 비동기작업처리할때 

<br>

##### promise객체가 rejected 상태일때 실행할 콜백 넣는법

방법 1.

then 메소드에 두번째 파라미터에 넣으면 된다.

.then((response) => response.text(), (error) => {console.log(error); })

방법 2.

.catch((error) => {console.log(error); })

catch메소드는 then 메소드를 약간 변형시킨 것

가장 마지막에 써야 하는게 맞지만, 작업을 살릴 방법이 있다면 중간에 catch 메소드를 써도 된다.

<br>

##### finally 메소드 => promise객체가 뭔상태든지 항상 실행하는 콜백함수 등록

.finally( ()=>{ console.log('exit'); }) ;

보통 catch 뒤에 쓴다.

<br>

### async / await

##### async 

: 비동기 실행이 될 내용이 있다는 뜻 그 부분은 함수 내부에서 await이 붙은 부분 

##### await 

:promise 객체를 리턴하는 코드 앞에 작성!

: 해당 promise객체가 **fullfiled상태**가 될때까지 기다림.

: async함수 안에서만 사용할 수 있다.

##### try-catch문

해당 promise 객체가 rejected상태일 때를 대비할수 있다.

try {

fullfiled일때 } catch (error) {

rejected상태 일때 } finally {

무슨 상태든 무조건 실행 }



### 
