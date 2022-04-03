# ppt 70~79 자체적으로 실습
# import 명령 표준 모듈
# 80 ~

# 외부의 모듈을 가져와 사용
# 필요 기능에 따라 선택
# 파이썬에는 자주 사용하는 기능이 표준 모듈로 함께 설치되어 있음
# math 모듈에 작성된 모든 상수와 함수를 가져옴
import time
from builtins import print
from math import sqrt
from math import ceil
from math import floor
# 임포트 받은 방법이 하나만 받아도 되고 부분적으로 받을수도 있다.
# ex) math.sqrt() , or sqrt()
# 이 경우 sqrt 외 math에 속한 다른 함수는 사용할 수 없음
# print(math.sqrt(2)) 불가능
print(sqrt(2))
print(ceil(5.2)) # 올림값
print(floor(5.2)) # 내림값


