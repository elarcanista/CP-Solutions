# https://www.hackerrank.com/challenges/priyanka-and-toys/
import math
_ = input()
arr = sorted(list(map(int, input().split())))
count = 0
min_item = -math.inf
for item in arr:
    if item > min_item + 4:
        count += 1
        min_item = item
print(count)
