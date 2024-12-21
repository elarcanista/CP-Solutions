# https://www.hackerrank.com/challenges/fair-rations/
n = int(input())
arr = list(map(lambda x: int(x) % 2, input().split()))
if sum(arr) % 2 == 1:
    print("NO")
else:
    count = 0
    for i in range(len(arr)-1):
        if arr[i] == 1:
            count += 2
            arr[i] = (arr[i] + 1) % 2
            arr[i+1] = (arr[i+1] + 1) % 2
    print(count)
