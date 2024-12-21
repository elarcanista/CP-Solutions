# https://www.hackerrank.com/challenges/30-review-loop/
n = int(input())
for i in range(n):
	s1 = ""
	s2 = ""
	str = input()
	i = 0
	for char in str:
		if i%2 == 0:
			s1 += char
		else:
			s2 += char
		i += 1
	print(s1, s2)
