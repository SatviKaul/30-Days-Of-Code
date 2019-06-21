class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
    
    def calculate(self):
        sum=0
        for x in range(0,len(scores)):
            sum = sum + scores[x]
        avg=(sum)/(len(scores))
        if avg>=90:
            return 'O'
        elif 80<=avg<90:
            return 'E'
        elif 70<=avg<80:
            return 'A'
        elif 55<=avg<70:
            return 'P'
        elif 40<=avg<55:
            return 'D'
        elif avg<40:
            return 'T'
line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) 
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
