data = list(map(int, input().split()))

a = (data[0]%10)*100 + (((data[0]%100)//10)*10) + (data[0]//100)
b = (data[1]%10)*100 + (((data[1]%100)//10)*10) + (data[1]//100)

if a > b:
    print(a)
elif a < b:
    print(b)

