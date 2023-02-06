N = int(input())
S = input()
A = S.count("A")
D = S.count("D")

if A == D:
    print("Friendship")
elif A > D:
    print("Anton")
else:
    print("Danik")