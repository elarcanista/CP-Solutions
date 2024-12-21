# https://www.hackerrank.com/challenges/30-sorting
import sys

def bubble(arr):
    totSwap = 0
    for i in range(len(arr)):
        numberOfSwaps = 0
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                numberOfSwaps+=1
        totSwap += numberOfSwaps
        if numberOfSwaps == 0:
            break
    print("Array is sorted in", totSwap, "swaps.")
    print("First Element:", arr[0])
    print("Last Element:", arr[-1])
    
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
bubble(a)
