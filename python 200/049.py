# 049 `class` basic
"""
클래스: 지정한 이름으로 만든 하나의 독립된 공간, 이름공간(name space)
클래스 멤버: 클래스에서 변수 역할, 클래스 메소드 밖에서 정의되는 변수
클래스 메소드: 클래스에서 함수와 동일한 역할, 클래스 내에서 정의되는 함수
"""

"""
class MyClass:                  # 클래스 이름: MyClass
    var = 'Hi there?'           # 클래스 멤버: var = 'Hi there?'

    def sayHello(self):         # 클래스 메소드: sayHello(self) 정의, self -> 인스턴스 객체를 가리키는 참조자
        print(self.var)         # sayHello()를 사용시 동작 정의


obj = MyClass()                 # 인스턴스 객체로 만들기 위해 `obj` 변수에 `MyClass()` 호출하여 지정
print(obj.var)
obj.sayHello()
"""


class MyClass:
    var = "Hi there!"

    def sayHello(self):
        param1 = "Hi!"
        self.param2 = "Hello?"
        print(param1)
        print(self.var)


obj = MyClass()
print(obj.var)
print(obj.param2)
obj.sayHello()

