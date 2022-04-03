# 93 ~ 97
# 클래스~

# 생성자
# __init__ 생성자
# 초기값으로 멤버변수를 초기화
# 객체 생성
# __init__의  첫 번째 인수 self로 전달
# 생성문에서 전달한 인수를 두 번째 이후의 인수로 전달

# class Human:
#     def __init__(Self, age, name):
#         Self.age = age
#         Self.name = name
#     def intro(Self):
#         print(str(Self.age) + "살 " + Self.name + "입니다.")
#
# kim = Human(25, "김도현")
# kim.intro()
#
# lee = Human(27, "이승환")
# lee.intro()

# 상속
# 기존 클래스 확장하여 멤버 추가하거나 동작 변경
# 클래스 이름 다음의 괄호 안에 부모 클래스 이름 지정

class Human:
    def __init__(Self, age, name):
        Self.age = age
        Self.name = name
    def intro(Self):
        print(str(Self.age) + "살 " + Self.name + "입니다.")

class Student(Human):
    def __init__(self, age, name, stunum):
        super().__init__(age, name)
        self.stunum = stunum
    def intro(Self):
        super().intro()
        print("학번은 : " + str(Self.stunum) + " 입니다.")
    def study(Self):
        print("Study ing~")


kim = Human(25, "김도현")
kim.intro()

lee = Student(27, "이승환", 1601034)
lee.intro()
lee.study()