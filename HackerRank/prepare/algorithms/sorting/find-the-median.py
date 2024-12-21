# https://www.hackerrank.com/challenges/find-the-median/
n = int(input())
arr = sorted(map(int, input().split()))
print(arr[n//2])
