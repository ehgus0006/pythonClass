# NumPy
# Numerical Python의 줄임말
# Numpy는 벡터 및 행렬 연산에 있어서 매우 편리한 기능을 제공
# 데이터분석 라이브러리인 pandas와 matplotlib의 기반으로 사용됨
# 기본적으로 array(행렬 개념)라는 단위로 데이터를 관리
#
# 설치
# pip install numpy
# 코랩(Colab)을 사용한다면 기본적으로 설치되어있음
#
# 사용
# 라이브러리를 불러올 때에는 import문을 사용
# import  numpy  as  np   # numpy 라이브러리를 np라는 이름 호출

import numpy as np

# 1차원 배열
a = np.array([0, 1, 2, 3])
print(a)
print(a.ndim, a.shape, a.size) # 1, (4, ), 4

# 2차원 배열
a = np.array([[0,1,2,3], [4,5,6,7], [8,9,10,11]])
print(a)
print(a.ndim, a.shape, a.size) # 1, (4, ), 4

# numpy 라이브러리

# numpy.arange(시작값, 끝값, 증감분)
a = np.arange(0,1,0.1)
print(a) # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
a = a.reshape(2, -1) # 2층으로 분할
print(a)

# numpy.zeros()
# 0으로 채워진 배열 만들기
a = np.zeros((2,3)) # 2*3형태 2차원 배열로 생성
print(a)

# numpy.ones()
# 1으로 채워진 배열 만들기
a = np.ones((2,3)) # 2*3 형태 2차원 배열로 생성
print(a)

# numpy.random.rand(개수)
# 0과 1사이의 무작위 수로 채워진 1차원 배열 만들기
a = np.random.rand(3) # 0~1사이의 3개의 무작위 수 생성
print(a)

# numpy.random.normal(평균, 표준편차, 개수)
# 정규분포를 가지며 지정된 평균과 표준편차를 갖는 1차원 배열 만들기
a = np.random.normal(1,2,10) # 평균 1, 표준편차 2, 개수 10
print(a)

# numpy.random.randint(시작값, 끝값, 개수)
# 시작값과 끝값 사이의 무작위 정수를 갖는 1차원 배열 만들기
a = np.random.randint(0,10,5) # 시작값 0, 끝값 10, 개수 5
print(a)