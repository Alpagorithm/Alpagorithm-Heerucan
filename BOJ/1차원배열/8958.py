# 어려웠음
n = int(input())

for i in range(n):
    counting = 0 # 횟수 변수
    total = 0
    string = list(str(input())) # 리스트로 문자 입력받고
    for letter in string:
        if letter == 'O': # O인 경우에는 1부터 1,2,3.. 카운트
            counting += 1
            # print(counting, "오")
        else:
            counting = 0 # X인 경우에는 0 을 더함
            # print(counting, "엑스")
        total += counting # O/X 카운팅 합치기
    print(total)


