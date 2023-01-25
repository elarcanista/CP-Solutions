import sys
 
TC = int(input())
tot = 0
for i in range(TC):
	sum = 0
	for sure in input().split():
		sum += int(sure)
	if sum >= 2 :
		tot += 1
print(tot)