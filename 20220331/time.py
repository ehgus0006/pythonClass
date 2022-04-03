import time

# ppt 83

# 날짜와 시간 관련 기능 제공
# 에폭(Epoch) / 유닉스 시간
print(time.time())

# 일상 시간 문자열으로 변환 가능
t = time.time()
print(time.ctime(t))

#  두 지점 간의 경과 시간 측정
start = time.time()
for a in range(1000):
    print(a)
end = time.time()
print(end - start)