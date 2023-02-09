N = int(input())
D = 256
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if N == 1918:
    d = days[0] + days[1] - 13
    for i in range(2, len(days)):
        if d + days[i] < D:
            d += days[i]
        else:
            print(D - d, f"{i+1:02d}", N, sep=".")
            break
elif N < 1918:
    d = 0
    for i in range(len(days)):
        if d + days[i] < D:
            d += days[i]
        else:
            if N % 4 == 0:
                d += 1
            print(D - d, f"{i+1:02d}", N, sep=".")
            break
elif N > 1918:
    d = 0
    for i in range(len(days)):
        if d + days[i] < D:
            d += days[i]
        else:
            if N % 4 == 0 and N % 100 != 0 or N % 400 ==0:
                d += 1
            print(D - d, f"{i+1:02d}", N, sep=".")
            break