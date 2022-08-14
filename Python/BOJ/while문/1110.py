# 도저히 모르겠어서 풀이 참고했음... 죽고시파

num = int(input())
firstInputNum = num
newNum = 0
cycle = 0
while True:
    a = num // 10
    b = num % 10
    x = (a+b)%10 # 더한 값의 일의자리
    newNum = (b*10) + x # 새로운 수
    cycle += 1 # 사이클 추가
    num = newNum # 다시 num에 newNum을 대입
    if newNum == firstInputNum: # 새로운 수가 가장 초기의 num(처음 입력한)과 같다면
        break
print(cycle)



