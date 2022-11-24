# 파이썬으로 배우는 웹 크롤러

[실습](https://github.com/Jung-YongHan/Crawling-for-Data-Analysis/tree/main/Web%20Crawler%20Learning%20with%20Python/Part%203_%EC%9B%B9%EC%9D%84%20%EA%B5%AC%EC%84%B1%ED%95%98%EA%B3%A0%20%EC%9E%88%EB%8A%94%20%EC%9A%94%EC%86%8C/Practice)

## 1. 웹
World Wide Web. WWW의 약자로 인터넷에 연결된 클라이언트들이 정보를 공휴할 수 있는 공간을 의미.  
이러한 공간을 사용할 수 있도록 해주는 것이 **웹 브라우저**.  
웹에서 보는 페이지 하나하나를 **웹 페이지**라고 하며 이러한 페이지가 모이면 **웹 사이트**를 이룸.  

\* 웹페이지 구성 요소
- 레이아웃을 잡아주는 **HTML**
- 기능을 불어넣어 주는 **JavaScript**
- 화면을 꾸며주는 **CSS**

크롤러를 만들기 위해서는 목표가 되는 웹 페이지의 구조를 이해하고 그 안에서 원하는 데이터를 찾아낼 수 있어야 함.  
그렇기 때문에 웹 페이지의 구성 요소인 HTML, CSS, JAvaScript에 대한 정확한 이해가 필요.

---
---
## 2. HTML
HyperText Markup Language. HTML의 약자로 웹을 이루고 있는 가장 기본이 되는 요소.  
HTML은 확장자가 HTML로 된 파일을 생성하여 실행하면 웹 페이지를 볼 수 있음.  
꺽쇠(<>)로 감싸져 있는 것을 **태그**라고 하고 여는 태그 <>, 닫는 태그</>로 구성.  
HTML에서는 여는 태그가 있으면 반드시 닫는 태그로 감싸주어야 함.
```html
    <meta name="Subject" content="홈페이지 주제">
    <meta name="Title" content="홈페이지 이름">
    <meta name="Description" content="설명문">
    <meta name="Keywords" content="키워드">
    <meta name="Author" content="만든 사람 이름">
    <meta name="Publisher" content="만든 단체나 회사">
    <meta name="Other Agent" content="웹 책임자">
    <meta name="Classification" content="카테고리 위치(분류)">
    <meta name="Generator" content="생성 프로그램(에디터)">
    <meta name="Reply-To(Email)" content="메일 주소">
    <meta name="Filename" content="파일 이름">
    <meta name="Author-Date" content="제작일">
    <meta name="Location" content="위치">
    <meta name="Distribution" content="배포자">
    <meta name="Copyright" content="저작권">
    <meta name="Robots" content="ALL">
```
meta 태그는 name과 content 속성으로 문서의 정보를 나타냄.  

style 태그는 CSS 코드가 포함되는 태그. link 태그도 CSS 코드가 담겨 있는 태그.  
두 태그의 차이점은 link 태그는 CSS 코드가 포함된 CSS 파일을 로드하는 태그.

scrpit 태그는 JavaScript 코드가 포함된 태그.  
style과 link와 다르게 script 태그로 JavaScript 코드를 작성하거나 JavaScript 코드가 포함된 파일을 로드할 수 있음.  
script 태그는 head 태그에 포함될 수 있지만 body 태그 가장 하단에 포함될 수 있음.

---
---
## 3. CSS
Cascading Style Sheets. CSS의 약자로, 웹 사이트를 꾸며주는 역할<br>
CSS로 웹사이트를 꾸며주기 위해 해당 태그에 접근하는 방식을 크롤러에서도 똑같이 적용할 수 있기 때문에 CSS를 배움.

- selector - CSS를 이용하여 꾸미기 위해 특정 요소에 접근하는 것.<br>
태그를 이용하는 방법과 id, class 속성을 이용하는 방법.

---
---
## 4. JavaScript
웹 사이트에 기능을 넣어 주며 script 태그를 이용하여 작성<br>
script 태그는 head에 들어가도 되지만, body의 가장 하단 부분에 넣어주는 것을 권장.<br>

자바스크립트에서 가장 중요한 점은 HTML 코드를 만들 수 있다는 점. 이렇게 생성된 HTML 코드는 크롤러가 접근하기 힘듦.
웹사이트에서 HTML로 기본적인 레이아웃만 잡고 JavaScript를 이용하여 서버로부터 데이터를 가져와 표시.

---
---
## 5. 웹 렌더링의 원리
웹 브라우저는 JavaScript 코드를 실행시킨 후 HTML을 DOM으로 표현

- DOM<br>
Document Object Model로 HTML을 시각적으로 쉽게 표현하기 위해 만든 객체. 즉, 문서를 구조화 시킨 것.<br>
태그 옆에 삼각형을 누르면 자식 태그를 열어볼 수 있도록 되어 있음. 이러한 구조를 DOM 구조라고 함.<br>
DOM은 크롤러를 만들 때 중요한 부분. 데이터를 수집하기 위해 DOM을 이용해 데이터를 접근 후 해당 데이터를 수집.<br>

    원래의 HTML코드를 크롤러가 가져오게 됨.  
    편의상 개발자 도구로 웹을 분서가지만 소스 보기 페이지에서 해당 요소가 있는지 확인해야함.
    만약 소스 보기 페이지에서 확인했는데 수집하고자 하는 요소가 없다면 [Network]탭을 이용하여 서버에서 데이터를 받아오는지 확인  
    그렇지 않을 경우 셀레니움(selenium)이라는 라이브러리를 사용하여 해결.