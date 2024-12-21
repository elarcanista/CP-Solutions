# https://www.hackerrank.com/contests/projecteuler/challenges/euler059/
import itertools as iter

def check(message, password):
    decoded = ""
    good = True
    for i in range(len(message)):
        C = message[i] ^ ord(password[i%3])
        decoded += chr(C)
        lower = ord("a") <= C and C <= ord("z")
        upper = ord("A") <= C and C <= ord("Z")
        digit = ord("0") <= C and C <= ord("9")
        special = C in map(ord, list("();:,.'?-! "))
        if not(lower or upper or digit or special):
            return False
    return True

lower = [chr(ascii) for ascii in range(ord("a"), ord("z")+1)]

N = int(input())
message = list(map(int, input().split()))
for password in iter.product(lower, repeat=3):
    if check(message, password):
        print("".join(password))
        break
