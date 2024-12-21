# https://www.hackerrank.com/challenges/30-nested-logic/
date1 = [int(i) for i in input().strip().split(" ")]
date2 = [int(i) for i in input().strip().split(" ")]
if date1[2] > date2[2]:
    print(10000)
elif date1[2] < date2[2]:
    print(0)
elif date1[1] > date2[1]:
    print(500*(date1[1]-date2[1]))
elif date1[1] < date2[1]:
    print(0)
elif date1[0] > date2[0]:
    print(15*(date1[0]-date2[0]))
else:
    print(0)
