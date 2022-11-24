# ���̽����� ���� �� ũ�ѷ�

[�ǽ�](https://github.com/Jung-YongHan/Crawling-for-Data-Analysis/tree/main/Web%20Crawler%20Learning%20with%20Python/Part%203_%EC%9B%B9%EC%9D%84%20%EA%B5%AC%EC%84%B1%ED%95%98%EA%B3%A0%20%EC%9E%88%EB%8A%94%20%EC%9A%94%EC%86%8C/Practice)

## 1. ��
World Wide Web. WWW�� ���ڷ� ���ͳݿ� ����� Ŭ���̾�Ʈ���� ������ ������ �� �ִ� ������ �ǹ�.  
�̷��� ������ ����� �� �ֵ��� ���ִ� ���� **�� ������**.  
������ ���� ������ �ϳ��ϳ��� **�� ������**��� �ϸ� �̷��� �������� ���̸� **�� ����Ʈ**�� �̷�.  

\* �������� ���� ���
- ���̾ƿ��� ����ִ� **HTML**
- ����� �Ҿ�־� �ִ� **JavaScript**
- ȭ���� �ٸ��ִ� **CSS**

ũ�ѷ��� ����� ���ؼ��� ��ǥ�� �Ǵ� �� �������� ������ �����ϰ� �� �ȿ��� ���ϴ� �����͸� ã�Ƴ� �� �־�� ��.  
�׷��� ������ �� �������� ���� ����� HTML, CSS, JAvaScript�� ���� ��Ȯ�� ���ذ� �ʿ�.

---
---
## 2. HTML
HyperText Markup Language. HTML�� ���ڷ� ���� �̷�� �ִ� ���� �⺻�� �Ǵ� ���.  
HTML�� Ȯ���ڰ� HTML�� �� ������ �����Ͽ� �����ϸ� �� �������� �� �� ����.  
����(<>)�� ������ �ִ� ���� **�±�**��� �ϰ� ���� �±� <>, �ݴ� �±�</>�� ����.  
HTML������ ���� �±װ� ������ �ݵ�� �ݴ� �±׷� �����־�� ��.
```html
    <meta name="Subject" content="Ȩ������ ����">
    <meta name="Title" content="Ȩ������ �̸�">
    <meta name="Description" content="����">
    <meta name="Keywords" content="Ű����">
    <meta name="Author" content="���� ��� �̸�">
    <meta name="Publisher" content="���� ��ü�� ȸ��">
    <meta name="Other Agent" content="�� å����">
    <meta name="Classification" content="ī�װ� ��ġ(�з�)">
    <meta name="Generator" content="���� ���α׷�(������)">
    <meta name="Reply-To(Email)" content="���� �ּ�">
    <meta name="Filename" content="���� �̸�">
    <meta name="Author-Date" content="������">
    <meta name="Location" content="��ġ">
    <meta name="Distribution" content="������">
    <meta name="Copyright" content="���۱�">
    <meta name="Robots" content="ALL">
```
meta �±״� name�� content �Ӽ����� ������ ������ ��Ÿ��.  

style �±״� CSS �ڵ尡 ���ԵǴ� �±�. link �±׵� CSS �ڵ尡 ��� �ִ� �±�.  
�� �±��� �������� link �±״� CSS �ڵ尡 ���Ե� CSS ������ �ε��ϴ� �±�.

scrpit �±״� JavaScript �ڵ尡 ���Ե� �±�.  
style�� link�� �ٸ��� script �±׷� JavaScript �ڵ带 �ۼ��ϰų� JavaScript �ڵ尡 ���Ե� ������ �ε��� �� ����.  
script �±״� head �±׿� ���Ե� �� ������ body �±� ���� �ϴܿ� ���Ե� �� ����.

---
---
## 3. CSS
Cascading Style Sheets. CSS�� ���ڷ�, �� ����Ʈ�� �ٸ��ִ� ����<br>
CSS�� ������Ʈ�� �ٸ��ֱ� ���� �ش� �±׿� �����ϴ� ����� ũ�ѷ������� �Ȱ��� ������ �� �ֱ� ������ CSS�� ���.

- selector - CSS�� �̿��Ͽ� �ٹ̱� ���� Ư�� ��ҿ� �����ϴ� ��.<br>
�±׸� �̿��ϴ� ����� id, class �Ӽ��� �̿��ϴ� ���.

---
---
## 4. JavaScript
�� ����Ʈ�� ����� �־� �ָ� script �±׸� �̿��Ͽ� �ۼ�<br>
script �±״� head�� ���� ������, body�� ���� �ϴ� �κп� �־��ִ� ���� ����.<br>

�ڹٽ�ũ��Ʈ���� ���� �߿��� ���� HTML �ڵ带 ���� �� �ִٴ� ��. �̷��� ������ HTML �ڵ�� ũ�ѷ��� �����ϱ� ����.
������Ʈ���� HTML�� �⺻���� ���̾ƿ��� ��� JavaScript�� �̿��Ͽ� �����κ��� �����͸� ������ ǥ��.

---
---
## 5. �� �������� ����
�� �������� JavaScript �ڵ带 �����Ų �� HTML�� DOM���� ǥ��

- DOM<br>
Document Object Model�� HTML�� �ð������� ���� ǥ���ϱ� ���� ���� ��ü. ��, ������ ����ȭ ��Ų ��.<br>
�±� ���� �ﰢ���� ������ �ڽ� �±׸� ��� �� �ֵ��� �Ǿ� ����. �̷��� ������ DOM ������� ��.<br>
DOM�� ũ�ѷ��� ���� �� �߿��� �κ�. �����͸� �����ϱ� ���� DOM�� �̿��� �����͸� ���� �� �ش� �����͸� ����.<br>

    ������ HTML�ڵ带 ũ�ѷ��� �������� ��.  
    ���ǻ� ������ ������ ���� �м������� �ҽ� ���� ���������� �ش� ��Ұ� �ִ��� Ȯ���ؾ���.
    ���� �ҽ� ���� ���������� Ȯ���ߴµ� �����ϰ��� �ϴ� ��Ұ� ���ٸ� [Network]���� �̿��Ͽ� �������� �����͸� �޾ƿ����� Ȯ��  
    �׷��� ���� ��� �����Ͽ�(selenium)�̶�� ���̺귯���� ����Ͽ� �ذ�.