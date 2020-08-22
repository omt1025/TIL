# CSS



## 1. 정의

- Cascading Style Sheets
- 문서를 표시하는 방법을 지정해주는 언어
- HTML안에서 사용 가능하지만 별도로 구분된 언어이다.
- 웹 브라우저는 내장 기본 스타일을 가지고 있어 CSS가 없어도 작동한다.
- CSS 구문
  - 선택자{ 선언, 속성:값 }
- 정의 방법
  1. 인라인(inline)
     - 해당 태그에 직접 `style` 속성을 준다.
  2. 내부 참조
     - head 태그 내에 `<style>`에 지정한다.
  3.  외부참조
     - 외부 CSS파일을 head의 link를 통해 불러온다.



## 2. CSS Selectors

> 특정 요소를 선택하여 스타일링하기 위해 탄생

### 1. 기초 선택자

- 전체 선택자, 타입 선택자
- 클래스 선택자, 아이디 선택자, 속성 선택자



### 2. 고급 선택자

- 자식 선택자, 자손 선택자
  - 자식 선택자 : 바로 하위에 있는 자식 요소
  - 자손 선택자 : 부모 선택자에 상속된 모든 자식 선택자
- 형제, 인접 형제 선택자



### 3. 의사 클래스(pseudo class)

- 링크, 동적 의사 클래스
- 구조적 의사 클래스



### 4. 적용 우선순위

1. !importance
   - 문제 확인을 위해 주로 사용
   - bootstrap에서 원하는 내용을 확인할 때 사용
   - 이외에는 잘 사용하지 않는다.
2. Inline 
   - 태그 안에 직접 스타일 속성을 사용
3. id 선택자
   - id는 중복되면 안되기 때문에 inline과 비슷한 효과가 나타남.
4. class 선택자
   - 가장 많이 사용
5. 요소 선택자
   - 범용적이라 우선 순위가 낮음
6. 소스 순서
   - 순서에 맞춰서 스타일이 적용됨



### 5. 상속

- 부모 요소의 속성을 자식에게 상속한다.
  - text, opacity, visibility등을 상속함.
  - Box model, position 등은 상속하지 않는다.



### 6. 단위

1. 크기 단위(상대적)
   1. px
   2. %
   3. **em** : 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
   4. **rem** : 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐, em의 상속의 영향으로 사이즈가 의도치 않게 변경되는 것을 방지하기 위해 rem을 기준으로 삼는다.
   5. Viewport 기준 단위 : vw, vh, vmin, vmax

2. 색상 단위
   1. 색상 키워드
   2. RGB 색상
      1. '#' + 16진수
      2. rgb( , , )
   3. HSL 색상



### 7. Box Model

> 모든 것은 box의 형태로 이루어져 있다!

1. 구성
   1. Margin : 테두리 바깥의 외부 여백, 배경색을 지정할 수 없음
   2. Border : 테두리 영역
   3. Padding : 테두리 안쪽의 내부 여백, 요소에 적용된 배경색이나 이미지가 적용되는 영역
   4. Content : 글이나 이미지 등 요소의 실제 내용
2. box-sizing
   1. content 영역만을 box로 지정
   2. 하지만 일반적으로 border까지의 영역을 보게됨, 이 경우 box-sizing을 border-box로 지정
3. 마진 상쇄(Margin collapsing)
   1. 인접 형제 요소 간의 margin이 겹쳐 보이게 될 경우



### 8. Display

1. 블록 레벨 요소
   - div / ul, ol, li / p / hr / form 등
   - display : block
     - 줄 바꿈이 일어남
     - 화면 전체의 가로 폭을 차지
     - 인라인 레벨 요소를 포함 가능
     - margin-right/left: auto
2. 인라인 레벨 요소
   - span / a / img / input, label / b, em, i, strong 등
   - display :  inline
     - 줄 바꿈이 일어나지 않음
     - content 너비만큼 가로 폭을 차지
     - 상하 여백은 line-height로 지정할 수 있고 나머지 요소들로 지정할 수 없음
     - text-align : center/right/left

3. inline-block
   - block과 inline의 특징을 모두 가짐



### 9. Position

1. static : 기본적으로 좌측 상단이 디폴트 값으로 가진다.
2. 부모 요소 내에서는 부모 요소를 기준으로 배치
3. 이동할 시
   1. relative : static 위치를 기준으로 이동(상대 위치)
   2. absolut : 가장 가까이 있는 부모/조상 요소를 기준으로 이동(절대 위치)
   3. fixed : 브라우저를 기준으로 이동(고정 위치)



### 10. Float

1. Float된 이미지를 텍스트로 둘러싸는 레이아웃
2. 이미지가 아닌 요소들에게도 적용
3. 속성
   1. none : 기본값
   2. left
   3. right



### 11. Flex

1. 메인 축과 교차 축에 유의 해야 한다!

2. 부모 요소에 flex를 선언
3. 배치 방향 설정 : flex-direction
   - 디폴트 값 : 왼쪽 -> 오른쪽 / 위 -> 아래
   - row / row-reverse / column / column-reverse
4. 메인 축 방향 설정 : justify-content
   1. flex-start : 배치 방향의 시작점부터
   2. flex-end : 배치 방향의 끝부터
   3. center : 중앙 정렬
   4. space-between : 양 끝 정렬
   5. space-around : 요소에 일정한 마진을 두어 정렬
   6. space-evenly : 일정한 간격 정렬
5. 교차 축 방향 설정 : align-items(한 줄) / content(여러 줄) / self(개별 요소)
   1. flex-start
   2. flex-end
   3. center
   4. baseline
6. flex-wrap : 항목들의 폭의 합이 컨테이너를 벗어나면 여러 행에 걸쳐서 나열 
7. flex-flow : flex-direction + flex-wrap