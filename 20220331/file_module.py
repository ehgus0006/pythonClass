# ppt 88 ~ 92

# 파일
# 정보를 저장하는 기본 단위
# 문서, 이미지, 멀티미디어 자료 등을 모두 보관

# 파일 오픈
# 파일 입출력 준비 및 파일 객체 반환
# 파일 사용 후 close 메서드로 닫기
# open(파일경로, 모드)

# r은 파일을 읽는다. 없으면 예외 발생
# w는 파일에 기록한다. 이미 파일이 있으면 덮어쓴다.
# a는 파일에 데이터를 추가한다.
# x는 파일에 기록하되 파일이 이미 있으면 실패한다.

# f = open("live.txt", "wt")
# f.write("Can you see me?")
# f.close()

# 파일 읽기

# try:
#     f = open("live.txt", "rt")
#     text = f.read()
#     print(text)
# except FileNotFoundError:
#     print("파일이 없습니다")
# finally:
#     f.close()
