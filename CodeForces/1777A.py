for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(arr)):
        if (arr[i-1] % 2) == (arr[i] % 2):
            ans += 1 
    print(ans)