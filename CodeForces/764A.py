# your code goes here

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a%b)
	
def lcm(a, b):
	return a*b//gcd(a,b)
	
a,b,c = map(int, input().split())
print(c//lcm(a,b))