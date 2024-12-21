# https://www.hackerrank.com/challenges/30-arrays/
import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.reverse()
if len(arr) > 0:
    print(arr[0], end="")
for i in arr[1:]:
    print("",i, end = "")
print()

