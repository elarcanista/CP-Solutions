# https://www.hackerrank.com/challenges/designer-pdf-viewer/
H = list(map(int, input().split()))
S = input()
h = 0
print(len(S) * max(map(lambda x: H[ord(x)-ord("a")], S)))
