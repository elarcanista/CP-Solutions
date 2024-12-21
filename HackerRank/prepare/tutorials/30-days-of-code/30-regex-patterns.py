# https://www.hackerrank.com/challenges/30-regex-patterns/
import sys
import re

N = int(input().strip())
dataBase = []
p = re.compile("(.)+@gmail.com")
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if p.match(emailID):
        dataBase.append(firstName)
dataBase.sort()
for i in dataBase:
    print(i)

