# HTML



## 1. 정의

- 웹 페이지를 작성하기 위한 언어
- W3C에서 웹 표준을 만든다.
- Hyper Text Markup Language
  - Hypertext?
    - 사용자에게 내용의 비순차적 검색이 가능하도록 제공되는 텍스트
    - 문서 내의 특정한 단어가 다른 단어나 데이터베이스와 링크되어 있어 사용자가 관련 문서를 넘나들며 원하는 정보를 얻을 수 있음.
  - Markup Language
    - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    - 일반적으로 데이터를 기술하는 정도로만 사용되어 프로그래밍 언어와는 구별됨.



## 2. 기본 구조 (.html)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>
    
</body>
</html>
```

### 1. head

- 해당 문서의 정보를 담고 있음.
- 브라우저에 나타나지 않아 사용자가 볼 수 없음.
- 의미적으로 구분한 것이므로 제목 이외에는 사용하지 않는 것을 권장함.
- Open Graph Protocol
  - 페이스북에서 최초로 정의한 메타 태그 규약
  - 링크를 공유하면 해당 내용의 이미지와 제목, 간단한 설명등을 표시
  - Metadata를 head영역에 추가하면 페이스북 bot이 해당 데이터를 읽어 내용을 표시할 수 있음.
  - 제목 / 데이터의 타입 / 사이트의 주소 / 이미지의 주소  

```html
<head>
<meta property="og:title" content="제목" />
<meta property="og:type" content="website" />
<meta property="og:url" content="http://주소" />
<meta property="og:image" content=”http://이미지.jpg" />
</head>
```



### 2. body

- 브라우저에 실제로 나타나는 정보
- DOM(Document Object Model)
  - W3C 공식 표준
  - 객체 지향 모델로써 구조화된 문서를 표현하는 형식
- element(요소)
  - `<h1>`요소는 태그와 내용으로 구성된다.`</h1>`
- attribute(속성)
  - 태그별로 사용할 수 있는 속성(attribute)은 다르다.
  - `=`사이에 공백은 사용하지 않고 `"`를 사용한다.
  - 모든 HTML 요소가 공통을 사용할 수 있는 속성
    - id, class, style, title
- 시맨틱 태그
  - 단순히 구역을 나누는 것이 아닌 의미 있는 정보의 그룹을 태그로 표현한 것
  - HTML5에서 의미론적 요소를 담은 태그가 등장
  - 주로 사용하는 태그
    - header : 문서 전체나 섹션의 헤더
    - nav : 네비게이션
    - aside : 사이드 공간
    - section : 컨텐트를 그룹으로 나누어 구분
    - article : 문서나 페이지 내에서 독립적으로 구분되는 영역
    - footer : 문서나 섹션의 마지막 부분
  - non semantic 요소로는 div, span등이 있음
  - input이나 imag같이 자체적으로 닫는 태그를 가진 태그가 존재



1. input type
   1. label과 주로 함께 사용하며 id값을 맞춰주어야 한다.
   2. 주로 쓰는 type
      1. text : 글자를 입력받음
      2. password : 비밀번호 방식으로 입력받음
      3. radio : 동그라미 형태의 체크박스
      4. checkbox : 네모 체크박스
      5. submit : 제출 버튼
2. select
   1. 드롭다운이 생김
   2. 아래에 option으로 아이템을 만들 수 있음
   3. 속성
      1. required : 반드시 선택을 하게 함, 선택하지 않으면 선택하라는 메세지창이 생김
      2. disabled : 사용자의 선택을 못하게 함
3. form
   1. action : submit했을 때 이동할 웹페이지를 나타냄



## 3. 문서 구조

### 1. 그룹

- `<p>` : 내용
- `<hr>` : 헤드라인 / `<br>` : 한줄 띄우기
- `<ol>`: 순서가 있는 리스트(1, 2, 3) /  `<ul>` : 순서가 없는 리스트
  - 자식 요소들로 `<li>`태그 사용
- `<div>` 



