# https://www.hackerrank.com/challenges/30-inheritance/
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
   def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
   def calculate(self):
        temp = 0
        for i in self.scores:
            temp += i
        temp /= len(scores)
        if 90 <= temp and temp <= 100:
            return "O"
        elif 80 <= temp and temp < 90:
            return "E"
        elif 70 <= temp and temp < 80:
            return "A"
        elif 55 <= temp and temp < 70:
            return "P"
        elif 40 <= temp and temp < 55:
            return "D"
        else:
            return "T"
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
