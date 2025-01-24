# https://www.hackerrank.com/challenges/mark-and-toys/
_, budget = map(int, input().split())
arr = sorted(list(map(int, input().split())))
count = 0
while count < len(arr) and budget >= arr[count]:
    budget -= arr[count]
    count += 1
print(count)
