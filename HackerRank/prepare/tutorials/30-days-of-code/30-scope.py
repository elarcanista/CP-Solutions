# https://www.hackerrank.com/challenges/30-scope/
class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        temp = 0
        for i in self.__elements:
            for j in self.__elements:
                temp = max(temp, abs(i-j))
        self.maximumDifference = temp
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
