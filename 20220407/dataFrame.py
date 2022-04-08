# 데이터프레임(DataFrame)
# 2차원 배열의 형태
# 여러 개의 시리즈(Series)를 모아 놓은 형태
#  엑셀이나 관계형데이터베이스 등에 사용

import pandas as pd

a = {'col0':[0,1,2], 'col1':[3,4,5], 'col2':[6,7,8]}
df = pd.DataFrame(a)
print(df)

#    col0  col1  col2
# 0     0     3     6
# 1     1     4     7
# 2     2     5     8

df = pd.DataFrame([[1, 100, 'A'], [2, 200, 'B']]
                  , index=['ABC','DEF'], columns=['번호', '점수', '반'])
print(df)

#      번호   점수  반
# ABC   1  100  A
# DEF   2  200  B

df.rename(columns={'점수':'신청'}, inplace=True)
print(df)

#      번호   신청  반
# ABC   1  100  A
# DEF   2  200  B

df.rename(index={'ABC':'가나다','DEF':'라마바'}, inplace=True)
print(df)

#   번호   신청  반
# 가나다   1  100  A
# 라마바   2  200  B

df.drop(['가나다'],axis=0, inplace=True)    # 행(row) 삭제
print(df)

df.drop(['신청', '반'],axis=1, inplace=True)   # 열(column) 삭제
print(df)

# 데이터프레임 행과 열 선택/추가/변경
# loc 대상 [인덱스 이름(index label)], 범위 범위의 끝을 포함
# loc 대상 [정수형 위치 인덱스(integer position)], 범위 범위의 끝을 제외외

a = {'타입A':[90,89,93],'타입B':[83,74,85], '타입C':[86,97,74]}
df = pd.DataFrame(a,index=['P1','P2','P3'])
print(df)

#     타입A  타입B  타입C
# P1   90   83   86
# P2   89   74   97
# P3   93   85   74

print(df.loc['P1'])
# 타입A    90
# 타입B    83
# 타입C    86
# Name: P1, dtype: int64

print(df.iloc[1:3])

#     타입A  타입B  타입C
# P2   89   74   97
# P3   93   85   74

print(df.iloc[1,2]) # 97
print(df['타입A']) # Name: 타입A, dtype: int64
print(df.iloc[[0,2],[0,1]]) # [행, 열]

#   타입A  타입B
# P1   90   83
# P3   93   85
df['타입D'] = 0               # '타입D' 열 추가
print(df)

# 타입A  타입B  타입C  타입D
# P1   90   83   86    0
# P2   89   74   97    0
# P3   93   85   74    0

df.loc['P4'] = [81,91,95,84]        # ＇P4＇  행 추가
print(df)

# 타입A  타입B  타입C  타입D
# P1   90   83   86    0
# P2   89   74   97    0
# P3   93   85   74    0
# P4   81   91   95   84

df.loc['P4','타입A'] = 100                # 값 변경
print(df)

#     타입A  타입B  타입C  타입D
# P1   90   83   86    0
# P2   89   74   97    0
# P3   93   85   74    0
# P4  100   91   95   84

df.drop(['타입D'],axis=1, inplace=True)
print(df)

#     타입A  타입B  타입C
# P1   90   83   86
# P2   89   74   97
# P3   93   85   74
# P4  100   91   95

print(df.sum(axis=1))   # 행방향 합

# P1    259
# P2    260
# P3    252
# P4    286
# dtype: int64

print(df.sum(axis=0))     # 열방향 합 df.sum(axis=0) == df.sum()

# 타입A    372
# 타입B    333
# 타입C    352
# dtype: int64

print(df.mean()) # 평균
# 타입A    93.00
# 타입B    83.25
# 타입C    88.00
# dtype: float64

df['A-B'] = df['타입A'] - df['타입B']
print(df)

#     타입A  타입B  타입C  A-B
# P1   90   83   86    7
# P2   89   74   97   15
# P3   93   85   74    8
# P4  100   91   95    9


df['A*B'] = df['타입A'] * df['타입B']
print(df)

# 타입A  타입B  타입C  A-B   A*B
# P1   90   83   86    7  7470
# P2   89   74   97   15  6586
# P3   93   85   74    8  7905
# P4  100   91   95    9  9100

# cs = pd.read_csv('K:\\data.csv',mode='w'
#    , encoding='euc-kr')

# 엑셀 파일 만들기
df.to_csv('D:\\excelPython\\data.csv',mode='w', encoding='euc-kr')
print(df)

# 타입A  타입B  타입C  A-B   A*B
# P1   90   83   86    7  7470
# P2   89   74   97   15  6586
# P3   93   85   74    8  7905
# P4  100   91   95    9  9100

df.sort_values(['A-B','A*B'],ascending=False,inplace=False)
print(df)

#  타입A  타입B  타입C  A-B   A*B
# P1   90   83   86    7  7470
# P2   89   74   97   15  6586
# P3   93   85   74    8  7905
# P4  100   91   95    9  9100

df['합']= df.sum(axis=1)
print(df)

df.to_csv('D:\\excelPython\\data1.csv',mode='w', encoding='euc-kr')