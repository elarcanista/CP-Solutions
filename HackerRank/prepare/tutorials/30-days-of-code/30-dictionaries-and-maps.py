# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/
import sys

n = int(input())
map = {}
for i in range(n):
	line = input().split()
	map[line[0]] = line[1]
for line in sys.stdin:
	line = line.strip()
	if line in map:
		print(line, "=", map[line], sep = "")
	else:
		print("Not found")
