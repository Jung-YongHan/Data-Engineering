# 파이썬으로 배우는 웹 크롤러

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
[실습 파일]()  
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