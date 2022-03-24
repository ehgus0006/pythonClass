# 사전
# 키와 값의 쌍을 저장하는 대용량 자료구조
# 맵 / 연관배열
# 중괄호 안에 키:값 현태로 콤마로 구분하여 나열

dic = {
    "boy" : "소년",
    "school" : "학교",
    "book" : "책"
}

# key
print(dic["boy"])
print(dic["book"])

# 찾는 키가 없을 경우 예외 발생
print(dic.get("student"))
print(dic.get("student", "사전에 없는 단어 입니다."))

# 사전 관리
# 실행 중 삽입, 삭제, 수정 등 편집 가능
dic = {
    "boy" : "소년",
    "school" : "학교",
    "book" : "책"
}
dic['boy'] = "소녀"
dic['school'] = "대학교"
del dic['book']
print(dic)

# 사전[키]
# 키의 존재 여부에 따라 동작 다름
# keys, values 메서드
dic = {
    "boy" : "소년",
    "school" : "학교",
    "book" : "책"
}

# 사전(key, value의 값을 출력할때는 list형태의 자료형으로 변환한 뒤 출력해야 한다) // ex) list(dic.keys())
print(dic.keys())
print(dic.values()) # dict_values(['소년', '학교', '책']) <- 형태로 출력 list 사용 안할 시
print(list(dic.items())) # key, value 만 출력

# dict * 객체
dic = {
    "boy" : "소년",
    "school" : "학교",
    "book" : "책"
}

# 두가지 값을 for 문에서 조회할 때 (key, val) 을 변수로 받는다.
keyList = dic.items()
for key, val in keyList:
    print(key, val)


# 집합 연산
twox = {2, 4, 6, 8, 10, 12}
threex = {3, 6, 9, 12, 15}

print("교집합", twox & threex) # 교집합 {12, 6}
print("합집합", twox | threex) # 합집합 {2, 3, 4, 6, 8, 9, 10, 12, 15}
print("차집합", twox - threex) # 차집합 {8, 2, 10, 4}
print("배타적 차집합", twox ^ threex) # 배타적 차집합 {2, 3, 4, 8, 9, 10, 15}




