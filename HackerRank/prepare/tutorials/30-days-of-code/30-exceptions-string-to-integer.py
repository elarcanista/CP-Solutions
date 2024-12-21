# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/
import sys

S = input().strip()
try:
    i = int(S)
    print(i)
except ValueError:
    print("Bad String")

