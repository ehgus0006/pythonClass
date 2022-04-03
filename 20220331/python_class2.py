# 98~107
# 클래스

# 액세서
# 파이썬 클래스의 멤버는 모두 공개되어 누구나 외부에서 액세스 가능
# 일정한 규칙 마련하고 안전한 액세스 보장
# 게터(Getter) 메서드
# 멤버 값 대신 읽음
# 세터(Setter) 메서드
# 멤버 값 변경

class Date:
    def __init__(self, month):
        self.month = month
    def getmonth(self):
        return self.month
    def setmonth(self, month):
        if 1 <= month <= 12:
            self.month = month

today = Date(8)
today.setmonth(15)
print(today.getmonth())

# 클래스 메서드
# 특정 객체에 대한 작업 처리하는 것이 아니라 클래스 전체에 공유
# @classmethod 데커레이터
# 첫 번째 인수로 클래스에 해당하는 cls 인수

class Car:
    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1
    @classmethod
    def outcount(cls):
        print(cls.count)
pride = Car("프라이드")
korando = Car("코란도")
Car.outcount()

# 정적 메서드
# 클래스에 포함되는 단순 유틸리티 메서드
# 특정 객체에 소속되거나 클래스 관련 동작 하지 않음
# @staticmethod 데커레이터

class Car:
    @staticmethod
    def hello():
        print("오늘도 안전 운행 합시다.")

    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1
    @classmethod
    def outcount(cls):
        print(cls.count)

Car.hello()

# 연산자 메서드
# 연산자 사용하여 객체끼리 연산
# 연산자 오버로딩
# 클래스별로 연산자 동작을 고유하게 정의

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

kim = Human(25, "김도현")
sang = Human(25, "김도현")
lee = Human(28, "이상진")

print(kim == sang)
print(kim == lee)


# 특수 메서드
# 특정한 구문에 객체 사용될 경우 미리 약속된 작업 수행

# __str__ str(객체) 형식으로 객체를 문자열 화한다.

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):
        return "이름 %s, 나이 %d" % (self.name, self.age)

kim = Human(26, "김도현")
print(kim)
