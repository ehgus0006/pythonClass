import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as pt
import pandas as pd

# 시리즈(Series)
# 1차원 배열의 형태
# 딕셔너리(dictionary), 리스트(list), 튜플(tuple)을 Series로 처리

a = {'key1':10, 'key2':20, 'key3':30, 'key4':40}
s = pd.Series(a)
plt.plot(s)
plt.show()

a = ['string', 100, True]
s = pd.Series(a) # 리스트를 시리즈로 변환
print(s)
# 0    string
# 1       100
# 2      True
# dtype: object

a = ('string', 100, True)
s = pd.Series(a) # 튜플을 시리즈로 변환
print(s)
# 0    string
# 1       100
# 2      True
# dtype: object