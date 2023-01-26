def sort(L):
    swaps = 0
    for i in range(1, len(L)):
        k = i
        while k > 0 and L[k-1] > L[k]:
            L[k-1], L[k] = L[k], L[k-1]
            k -= 1
            swaps += 1
    return swaps

N = input()
L = list(map(int, input().split()))
print(sort(L))