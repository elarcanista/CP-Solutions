def ans_min(prev, len_N, sum_N, start = 0):
    mean = sum_N/len_N
    if sum_N < start:
        return False
    
    if mean > 9:
        return False
    
    if len_N == 1 and sum_N <= 9:
        return prev + str(sum_N)
    
    for i in range(start, 10):
        next = ans_min(prev + str(i), len_N-1, sum_N - i)
        if next:
            return next
    return False

def ans_max(prev, len_N, sum_N, start = 0):
    mean = sum_N/len_N
    if sum_N < start:
        return False
    
    if mean > 9:
        return False
    
    if len_N == 1 and sum_N <= 9:
        return prev + str(sum_N)
    
    for i in reversed(range(start, 10)):
        next = ans_max(prev + str(i), len_N-1, sum_N - i)
        if next:
            return next
    return False


len_N, sum_N = map(int, input().split())

ans1 = ans_min("", len_N, sum_N, 1)
if not ans1:
    ans1 = -1

ans2 = ans_max("", len_N, sum_N, 1)
if not ans2:
    ans2 = -1

if len_N == 1 and sum_N == 0:
    print(0, 0)
else:
    print(ans1, ans2)