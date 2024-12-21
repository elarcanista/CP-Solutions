# https://www.hackerrank.com/challenges/30-binary-numbers/
n = int(input().strip())
maxn = 0
counter = 0
while n != 0:
	if n & 1 != 0:
		counter += 1
	else:
		maxn = max(maxn, counter)
		counter = 0
	n = n >> 1
maxn = max(maxn, counter)
print(maxn)

