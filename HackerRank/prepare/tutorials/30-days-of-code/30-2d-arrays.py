# https://www.hackerrank.com/challenges/30-2d-arrays/
import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
sum = arr[1][1]
sum += arr[0][0] + arr[0][1] + arr[0][2]
sum += arr[2][0] + arr[2][1] + arr[2][2]
        
for i in range(1,len(arr)-1):
    for j in range(1,len(arr)-1):
        temp = arr[i][j]
        temp += arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
        temp += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
        sum = max(sum, temp)
print(sum)

