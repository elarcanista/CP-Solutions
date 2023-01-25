n = int(input())
nums = list(map(int, input().split()))

flag = True
for i in range(len(nums)):
  if i == len(nums)/2:
    flag = not flag
  if flag:print(nums[n-i-1], end = " ")
  else:print(nums[i], end = " ")
  flag = not flag