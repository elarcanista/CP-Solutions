# https://www.hackerrank.com/challenges/two-arrays/
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = sorted(list(map(int, input().split())), reverse = True)
    good = True
    for i in range(n):
        if arr1[i] + arr2[i] < k:
            good = False
            break
    print(("NO", "YES")[good])
