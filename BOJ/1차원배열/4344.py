n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    people = 0
    for score in nums[1:]:
        if score > avg:
            people += 1
    rate = people/nums[0] *100
    print(f'{rate:.3f}%')