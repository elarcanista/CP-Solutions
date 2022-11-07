digits = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Fourty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "Hundred",
    1000: "Thousand",
    10**6: "Million",
    10**9: "Billion"
}

def parse(N):
    if N >= 10**9:
        triplet = N//(10**9)
        return f"{parse(triplet).strip()} {digits[10**9]} {parse(N - triplet * 10**9).strip()}"
    if N >= 10**6:
        triplet = N//(10**6)
        return f"{parse(triplet).strip()} {digits[10**6]} {parse(N - triplet * 10**6).strip()}"
    if N >= 10**3:
        triplet = N//(10**3)
        return f"{parse(triplet).strip()} {digits[10**3]} {parse(N - triplet * 10**3).strip()}"
    if N >= 100:
        first = N//100
        return f"{digits[first]} {digits[10**2]} {parse(N - first * 100).strip()}"
    if N >= 20:
        first = N//10
        return f"{digits[first * 10]} {parse(N - first * 10).strip()}"
    if N >= 1:
        return digits[N]
    return ""

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    if N == 0:
        print("Zero")
    elif N == 10**12:
        print("One Trillion")
    else:
        print(parse(N))