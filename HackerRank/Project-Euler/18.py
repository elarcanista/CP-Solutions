#Author: Andres Felipe Ortega Montoya - Luis Miguel Marin Loaiza
#HackerRank Project Euler #18 - Maximum path sum I
def maxsum(i,l):
	print(i,l)
	if l >= n:
		return list[i]
	else:
		return max(maxsum(i+l,l+1), maxsum(i+l+1,l+1)) + list[i]

tc = int(input().strip())
for i in range(tc):
	n = int(input().strip())
	list = []
	for j in range(n):
		list += [int(i) for i in input().strip().split(" ")]
	print(maxsum(0,1))
