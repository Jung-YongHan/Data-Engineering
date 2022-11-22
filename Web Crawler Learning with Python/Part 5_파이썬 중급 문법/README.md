# 파이썬으로 배우는 웹 크롤러

## 2. 클래스
- self 참조자<br>
객체가 메소드를 호출할 때 어느 객체가 호출할 것인지 알려주는 키워드<br>
이 키워드가 없다면 객체가 메소드 및 속성을 사용할 때 누가 호출한 것인지 알 수 없기 때문에 정상적으로 실행되지 않음.  

    -클래스에 메소드 첫 번째 인자가 self인 이유는 해당 메소드를 호출한 객체를 의미하기 때문.  

    -객체가 메소드를 호출할 대는 생성된 객체가 직접 호출하기 때문에 self가 필요 없음.  
    -직접 호출된 메소드가 다른 메소드를 호출할 때는 self를 명시해 주어야 해당 객체의 속성을 사용할 수 있다.

메소드 이름 앞에 언더바(_)가 2개 있으면 이 메소드는 생성된 객체를 호출하지 말라는 의미.  
타 언어와 달리 python은 모든 것이 public이기 때문에 이름에 암묵적 명시<br><br>

- \_\_call\_\_() - 객체를 호출할 때 실행하는 메소드 (타 언어에서 run 같은 기능)
- 속성은 []를 사용하여 속성에 접근할 수도 있음. a['hp']
- \_\_getitem\_\_() - [] 속성에 접근할 때 호출하는 메소드. ['']에 명시된 키 값을 인자로 받아 return. 직접 구현시켜 주어야 함.<br><br>

* 아래와 같이 속성을 dict형태로 구현 가능
```python
class charactor:

    def__init__(self, hp, attack, defence):
        self.info = {
            'hp' = hp,
            'attack' = attack,
            'defence' = defence,
        }

        print('player가 생성되었습니다')

    def __call__(self):
        print(f"hp: {self.hp}, attack: {self.attack}, defence: {self.defence}")
    
    def __getitem__(self, name):
        if name in self.info.keys():
            return slef.info[name]
        else:
            return "존재하지 않는 키값입니다."
```

- 스태틱 메소드, 클래스 변수

    파이썬에서는 클래스를 객체 생성의 도구가 아닌 네임스페이스를 목적으로 사용할 수 있다.  
    클래스가 단순히 네임스페이스 역할을 하기 때문에 self 인자를 받지 않음.  
    일반 함수처럼 사용하면 되지만, 클래스 내부에 속해 있기 때문에 [클래스.메소드] 형태로 사용
``` python 
class namespace1:
    @staticmethod
    def s1():
        print('namespace1 s1스태틱 메소드')
    
    @staticmethod
    def s2():
        print('namespace1 s2스태틱 메소드')

class namespace2:
    @staticmethod
    def s1():
        print('namespace2 s1스태틱 메소드')
    
    @staticmethod
    def s2():
        print('namespace2 s2스테틱 메소드')

namespace1.s1()
namespace2.s2()
```

- 클래스 변수

    모든 객체가 하나의 변수에 접근하는 방식으로 self가 아닌 클래스명으로 접근.  
    객체에 생성되는 것이 아닌 클래스 자체에 한 번 생성되기 때문에 클래스명으로 접근  
    ex) 객체가 총 몇 개가 생성이 되었는지 확인

- 상속  

    자식 클래스의 생성자가 호출 될 때 부모 클래스의 생성자도 같이 호출되어야 함.
    ```python
    class unit:
        uint_cnt = 0

        def __init__(self):
            print('unit 생성')
            unit.unit_cnt += 1
        
        def move(self):
            print('unit move')

    class bird(unit):

        def __init__(self):
            print('bird 생성')
            super(bird, self).__init__() # super(해당 클래스명, self).__init__()을 자식 생성자에 넣어주면 호출 시 부모 생성자도 호출

    class ground(unit):

        def __init__(self):
            print('ground 생성')
            super(ground, self).__init__()

    b1 = bird()
    b3 = bird()
    b1.move()
    g1 = ground()
    print(unit.unit_cnt)
    ```
---
---

## 3. 모듈

- pip(python package index)를 이용하여 다양한 패키지(모듈) 다운.
- 스크립트 언어에서는 파일을 객체 취급하기 때문에 import 시 해당 파일을 객체 취급 => 변수 접근 시 마침표(.)을 이용
- as(alias)로 네이밍 중복 방지 가능  

- \_\_name\_\_은 실행된 파일일 경우 __main__을 반환하고 import된 파일은 해당 파일의 이름을 반환한다. [실습]()

- 예외 처리  
    
    try~except 뿐만 아니라 else와 finally를 통해 기능 확장 가능  
    else는 try 부분이 정상적으로 완료되었을 때 실행되는 부분  
    finally는 최종적으로 무조건 실행되는 부분  
    raise를 통해 강제로 에러를 발생시켜 예외처리 가능(함수가 인자를 사용함에 있어 외부의 데이터에 의존적이기 때문에 함수 내부에서 사용하는 타입, 범위 등은 에러를 통해 엄격하게 관리)