# https://www.hackerrank.com/challenges/divisible-sum-pairs/
n, k = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if (nums[i]+nums[j])%k == 0:
            count+=1
print(count)
