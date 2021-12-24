# 답안 참고
s = input().upper()
setS = list(set(s)) # 중복없는 리스트
countList = [] # 글자수 리스트

for i in setS:
    countList.append(s.count(i)) # 중복이 있는 글자수 세서 추가

if countList.count(max(countList)) > 1: # 글자수 리스트 중 최대값이 4라고 할 때
    # 해당 원소를 가지고 있는 값이 여러개이면 중복이 있다는 것이니까 ?를 반환한다.
    print("?")
else:
    print(setS[countList.index(max(countList))]) # index가 위치 알려주는 메소드