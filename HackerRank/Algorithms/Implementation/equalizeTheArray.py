n = int(input())
nums = list(map(int, input().split()))
nums.sort()
last = nums[0]
maxi = 1
current = 1
print(nums)
for i in range(1,n):
    if last == nums[i]:
        current += 1
    else:
        maxi = max(maxi, current)
        current = 1
        last = nums[i]
maxi = max(maxi, current)
print(n-maxi)
